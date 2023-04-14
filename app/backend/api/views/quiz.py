import random
from collections import Counter
from django.shortcuts import get_object_or_404
from django.http import HttpResponseBadRequest, JsonResponse, HttpRequest, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from api.serializers import QuizAnswerSerializer, QuizSerializer, QuizFinishedSerializer, GetQuizReviewNewSerializer, GetTestSerializer
from moelasware.models import Quiz, QuizAnswer, User, Tag, Review, Test
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as AuthUser

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import fromstring, ElementTree

@api_view(["GET"])
def get_quiz_view(request, pk):
    # get a test with all the quizzAnswers attached to it
    if pk is not None:
        instance = get_object_or_404(Test, pk=pk)
        serializer = GetTestSerializer(instance, many=False)

        # get all the Quizzes for this test
        quizzes = Quiz.objects.filter(test__id=pk)
        quizzes_serializer = QuizSerializer(quizzes, many=True)

        # for each quiz get all the answers
        for quiz in quizzes_serializer.data:
            answers = QuizAnswer.objects.filter(quiz__id=quiz["id"])
            answers_serializer = QuizAnswerSerializer(answers, many=True)
            quiz["answers"] = answers_serializer.data

        return JsonResponse(
            {"test": serializer.data, "quizzes": quizzes_serializer.data}
        )

    return JsonResponse(
        {"invalid": "not good data"}, status=status.HTTP_400_BAD_REQUEST
    )


@api_view(["GET"])
def get_total_number_of_quizzes_view(request):
    count = Quiz.objects.can_be_added_to_a_test().count()
    return JsonResponse({"quizzes_count": count})


@api_view(["POST"])
@login_required
def get_n_quizzes_view(request):
    # If no quizzes are sent in the request -> quizzes are selected randomly
    # User gave config (num_quizes, allowed_tags (optional))

    if not "num_quizzes" in request.data.keys():
        return HttpResponseBadRequest("You must provide the number of quizzes")

    try:
        num_quizzes = int(request.data.get("num_quizzes"))
    except ValueError:
        return HttpResponseBadRequest(
            f"The number of quizzes must be a number and not {request.data.get('num_quizzes')}"
        )

    tags = request.data.get("allowed_tags")
    # print(tags)
    all_quizzes = Quiz.objects.can_be_added_to_a_test().order_by("?")

    quizzes_set = []
    if not tags:
        quizzes_set = all_quizzes.all()[:num_quizzes]
    else:
        n_tags = len(tags)
        fraction = int(num_quizzes / n_tags)
        rest = int(num_quizzes % n_tags)

        # criar lista de tags = [ (<TAG_TEXT>, <NUM_QUIZZES_WITH_TAG>), ...]
        tag_count = {}
        for tag in tags:
            tag_count[tag] = all_quizzes.filter(tags__text=tag).distinct().count()
        tags = sorted(
            tag_count.items(), key=lambda x: x[1]
        )  # ordenar da tag com menos quizzes para as que têm mais

        # Para cada tag tentar adicionar uma fracao -> se não houver suficientes tenta-se obter o que falta em quizzes com a proxima tag
        for tag in tags:
            tag_fraction = fraction + rest
            rest = 0
            quizzes_count = tag[1]

            added_quizzes = 0
            quizzes_with_tag = list(all_quizzes.filter(tags__text=tag[0]).distinct())

            # Percorrer os quizzes com a tag e adicionar quizzes que ainda nao estejam no quizzes_set
            for i in range(quizzes_count):
                if added_quizzes == tag_fraction:
                    break

                if quizzes_with_tag[i] not in quizzes_set:
                    quizzes_set.append(quizzes_with_tag[i])
                    added_quizzes = added_quizzes + 1

            rest = tag_fraction - added_quizzes

        if rest:
            return HttpResponseBadRequest(
                "There aren't enough quizzes with the given tags"
            )

    # Not enough quizzes that meet the specs
    if len(quizzes_set) < num_quizzes:
        return HttpResponseBadRequest(
            "The number of requested quizzes is bigger than the number of existing quizzes meeting the given specifications"
        )

    quizzes_serializer = QuizSerializer(quizzes_set, many=True)

    return JsonResponse({"quizzes": quizzes_serializer.data})


@api_view(["GET"])
def get_answers_for_quiz_view(request, quiz_id):
    answers_set = QuizAnswer.objects.filter(quiz__id=quiz_id).order_by("id")

    answers_serializer = QuizAnswerSerializer(answers_set, many=True)

    return JsonResponse({"answers": answers_serializer.data})


def quiz_finished_serializer_handler(data):
    quiz_list = []
    for i in data:
        quiz_list.append(
            [
                i["id"],
                i["name"],
                i["tags"],
                i["number_of_reviews_done"],
                i["review_result"],
            ]
        )
    return quiz_list


@api_view(["GET"])
@login_required
def get_user_quizzes_view(request):

    user = request.user
    quizzes = Quiz.objects.filter(author__user__username = user).filter(finished = True)

    if not quizzes.exists():
        return JsonResponse({"error":True, "message":"No finished quizzes found"})
    quizzes = QuizFinishedSerializer(quizzes, many = True).data
    quizzes = quiz_finished_serializer_handler(quizzes)

    return JsonResponse({"list_of_quizzes": quizzes, "error":False, "message":""})


def handle_frontend_fields(dataRequest):
    data = {'name': dataRequest['name'],
            'question': dataRequest['question'],
            'description' : dataRequest['description'],
            'tag' : dataRequest['tag'],
            'correct' : dataRequest['correct'],
            "answers": [], "justification": []
        }
    option_list = ["option1", "option2", "option3", "option4", "option5", "option6"]
    justification_list = [
        "justification1",
        "justification2",
        "justification3",
        "justification4",
        "justification5",
        "justification6",
    ]

    for i in option_list:
        if i in dataRequest:
            data["answers"].append(dataRequest[i])
        else:
            data["answers"].append("")

    for i in justification_list:
        if i in dataRequest:
            data["justification"].append(dataRequest[i])
        else:
            data["justification"].append("")

    return data


@api_view(["POST"])
def create_quiz_view(request):

    dataRequest = request.data["inputs"]
    data = handle_frontend_fields(dataRequest)

    if "name" not in data or data["name"] == "":
        # return HttpResponseBadRequest("Quiz name not inserted")
        return JsonResponse({"resposta": "Quiz name not inserted"})

    quiz = Quiz.objects.filter(name=data["name"])

    if quiz.exists():
        # return HttpResponseBadRequest(f"Quiz {data['name']} already exists")
        return JsonResponse({"resposta": f"Quiz {data['name']} already exists"})

    author = User.objects.get(user__username=request.user)
    quiz = Quiz(name=data["name"], author=author)
    quiz.save()
    for i in range(0, 6):
        quiz_answer = QuizAnswer(
            quiz=quiz,
        )
        quiz_answer.save()

    quiz_answers = QuizAnswer.objects.filter(quiz=quiz).order_by("id")

    for i in data:
        match i:
            case "description":
                if type(data["description"]) is str:
                    quiz.description = data["description"]

            case "question":
                if type(data["question"]) is str:
                    quiz.question = data["question"]

            case "tag":
                if type(data["tag"]) is str:
                    if len(data["tag"]) > 0:
                        tag = Tag.objects.filter(text=data["tag"])
                        if tag.exists():
                            tag = tag[0]
                            quiz.tags.add(tag)
                    else:
                        for j in quiz.tags.all():
                            quiz.tags.remove(i)
                else:
                    # return HttpResponseNotFound("Wrong Data for Tags Field")
                    return JsonResponse({"resposta": "Wrong Data for Tags Field"})

            case "answers":
                if type(data["answers"]) is list and len(data["answers"]) > 0 and len(data["answers"]) <= 6:
                    for j in range(len(data["answers"])):
                        answer = quiz_answers[j]
                        answer.text = data["answers"][j]
                        answer.save()

                elif type(data["answers"]) is not list:
                    # return HttpResponseNotFound("Wrong Data for Answers Field")
                    return JsonResponse({"resposta": "Wrong Data for Answers Field"})
                elif len(data["answers"]) == 0:
                    for j in range(len(quiz_answers)):
                        answer = quiz_answers[j]
                        answer.text = ""
                        answer.save()

            case "justification":
                if type(data["justification"]) is list and len(data["justification"]) > 0 and len(data["justification"]) <= 6:
                    for j in range(len(data["justification"])):
                        answer = quiz_answers[j]
                        answer.justification = data["justification"][j]
                        answer.save()
                elif type(data["justification"]) is not list:
                    return JsonResponse(
                        {"resposta": "Wrong Data for Justification Field"}
                    )
                    # return HttpResponseNotFound("Wrong Data for Justification Field")
                elif len(data["justification"]) == 0:
                    for j in range(len(quiz_answers)):
                        answer = quiz_answers[j]
                        answer.justification = ""
                        answer.save()

            case "correct":
                if type(data["correct"]) is str and len(data["correct"]) > 0:
                    correct = int(data["correct"][len(data["correct"]) - 1])
                    answers = QuizAnswer.objects.filter(quiz=quiz).order_by("id")
                    for i in range(1, len(answers) + 1):
                        if i == correct:
                            answers[i - 1].correct = True
                            answers[i - 1].save()
    quiz.save()

    quizzes = QuizAnswer.objects.filter(quiz=quiz).order_by('id')

    if request.data["flag"]:
        response = finish_quiz(quiz, quizzes)

    else:
        response = {"resposta": "Saved as Draft"}

    return JsonResponse(response)


@api_view(["PATCH"])
@login_required
def edit_quiz_view(request, id):

    dataRequest = request.data["inputs"]["info"]

    answers = []
    for i, j in request.data["inputs"].items():
        if i != "info":
            answers.append({"answer": j})

    quiz = Quiz.objects.filter(id=id)

    if not quiz.exists():
        return JsonResponse("Quiz not found or already finished")
        # return HttpResponseNotFound('Quiz not found or already finished')

    quiz = quiz[0]

    new_name = Quiz.objects.filter(name=dataRequest["name"]).filter(author=quiz.author)

    if new_name.exists() and quiz.name != new_name[0].name:
        # return HttpResponseNotFound(f"Quiz {data['name']} already exists")
        return JsonResponse(f"Quiz {dataRequest['name']} already exists")

    author = User.objects.filter(user__username=request.user)

    if author.exists() and author[0] != quiz.author:
        # return HttpResponseNotFound('Author not allowed to edit this quiz')
        return JsonResponse("Author not allowed to edit this quiz")

    elif not author.exists():
        # return HttpResponseNotFound('Author not found')
        return JsonResponse("Author not found")

    author = author[0]
    quiz_answers = QuizAnswer.objects.filter(quiz=quiz).order_by("id")

    for i in dataRequest:
        match i:
            case "name":
                if type(dataRequest["name"]) is str and dataRequest["name"] != "":
                    quiz.name = dataRequest["name"]
                elif dataRequest["name"] == "":
                    # return HttpResponseNotFound("Invalid name for quiz")
                    return JsonResponse("Invalid quiz name")

            case "description":
                if (
                    type(dataRequest["description"]) is str
                    and dataRequest["description"] is not None
                ):
                    quiz.description = dataRequest["description"]
                else:
                    # return HttpResponseNotFound("Wrong Data for Description Field")
                    return JsonResponse("Wrong Data for Description Field")

            case "question":
                if (
                    type(dataRequest["question"]) is str
                    and dataRequest["question"] is not None
                ):
                    quiz.question = dataRequest["question"]
                else:
                    # return HttpResponseNotFound("Wrong Data for Question Field")
                    return JsonResponse("Wrong Data for Question Field")

            case "tag":
                if type(dataRequest["tag"]) is str:
                    if len(dataRequest["tag"]) > 0:
                        tag = Tag.objects.filter(text=dataRequest["tag"])
                        if tag.exists():
                            tag = tag[0]
                            quiz.tags.add(tag)
                    else:
                        for j in quiz.tags.all():
                            quiz.tags.remove(i)
                else:
                    #return HttpResponseNotFound("Wrong Data for Tags Field")
                    return JsonResponse("Wrong Data for Tags Field")

            case "correct":
                if (type(dataRequest["correct"])) is str and dataRequest["correct"] != "undefined":
                    correct_option = int(dataRequest["correct"])
                    if correct_option > 0 and correct_option <= 6:
                        for j in range(len(quiz_answers)):
                            if j + 1 == correct_option:
                                quiz_answers[j].correct = True
                            else:
                                quiz_answers[j].correct = False
                            quiz_answers[j].save()

    for i in range(len(answers)):
        if (
            type(answers[i]["answer"]) is dict
            and "option" in answers[i]["answer"]
            and "justification" in answers[i]["answer"]
        ):
            answer = quiz_answers[i]
            answer.text = answers[i]["answer"]["option"]
            answer.justification = answers[i]["answer"]["justification"]
            answer.save()

    if quiz.rejected:
        quiz.rejected = False
    quiz.save()
    quizzes = QuizAnswer.objects.filter(quiz=quiz)
    if request.data["flag"]:
        response = finish_quiz(quiz, quizzes)

    else:
        response = {"resposta": "Saved as Draft"}
    return JsonResponse(response)

def finish_quiz(quiz: Quiz, quiz_answers: list):

    quiz_ready = False
    quiz_answers_ready = True
    correct_answer = False
    if (
        quiz.name != ""
        and quiz.tags.all().count() > 0
        and quiz.question != ""
        and quiz.description != ""
        and quiz.author is not None
    ):
        quiz_ready = True

    for i in quiz_answers:
        if i.text == "" or i.justification == "":
            quiz_answers_ready = False
        if i.correct:
            correct_answer = True

    flag = False
    if not correct_answer or not quiz_ready or not quiz_answers_ready:
        response = {"resposta": f"Your quiz {quiz.name} has been saved"}
        flag = False
        # response = {'resposta' : f"Your quiz has been saved (unfinished){[quiz.name, quiz.id]}"}
    else:
        response = {"resposta": f"Your quiz {quiz.name} has been finished successfully"}
        flag = True
        # response = {'resposta' : f"Your quiz has been finished successfully{[quiz.name, quiz.id]}"}

    if flag:
        Review.objects.filter(quiz = quiz).delete()
        users = User.objects.exclude(user__username = quiz.author.user.username)
        users = list(users)
        users_filtered = []
        for i in users:
            if Quiz.objects.filter(author = i).count() > 0:
                users_filtered.append(i)
                
        reviewers_list = random.sample(users,3)
        reviewers_list = random.sample(users_filtered,3)

      
        for i in reviewers_list:
            review = Review(
                reviewer=i,
                quiz=quiz,
            )
            review.save()

        quiz.finished = True
        quiz.save()

    return response


def handle_get_unapproved_quizzes_reviews_view(obj):
    info_review = []

    for i in obj:
        reviewer = i["reviewer"]["user"]["username"]
        id = i["id"]
        creation_date = i["creation_date"]
        comment = i["comment"]
        review_result = i["review_result"]
        info_review.append([id, reviewer, comment, creation_date, review_result])

    return info_review


@api_view(["GET"])
@login_required
def get_reviews_of_a_quiz_view(request, id):

    user = request.user
    quiz = Quiz.objects.filter(id=id).filter(author__user__username=user)

    if not quiz.exists():
        return HttpResponseBadRequest("Quiz not found")

    quiz = quiz[0]

    reviews = Review.objects.filter(quiz=quiz).filter(pending=False)

    if not reviews.exists():
        return JsonResponse({"error": True})
        # return HttpResponseBadRequest('No Reviews found')

    serializer = GetQuizReviewNewSerializer(reviews, many=True).data
    serializer = handle_get_unapproved_quizzes_reviews_view(serializer)

    return JsonResponse({"error": False, "reviews": serializer})


@api_view(["POST"])
def import_xml(request: HttpRequest):
    """Read the XML file.

    Arguments: HttpRequest
    Returns: JsonResponse
    """
    user = AuthUser.objects.filter(username="admin").first()
    if user is None:
        auth_user = AuthUser.objects.create_user(username="admin", password="admin")
        user = User.objects.create(user=auth_user)
        user.save()
    else:
        user = User.objects.filter(user=user).first()

    # Get the XML file from the request
    try:
        print(request.FILES)
        xml = request.FILES["xml"]
    except:
        return HttpResponseBadRequest("No XML file found", content_type="text/plain")

    # Replace A&D with AD in the XML file
    xml = xml.read().decode("utf-8").replace("A&D", "AD")

    # Parse the XML file
    try:
        tree = ElementTree(fromstring(xml))
        root = tree.getroot()
    except:
        return HttpResponseBadRequest("Invalid XML file", content_type="text/plain")

    try:
        for pergunta in root.findall("./perguntas"):

            for item in pergunta:
                tags = []

                for tag in item.findall("./tags/tag"):
                    if tag.text == "AD":
                        tag.text = "A&D"  # Replace AD with A&D

                    # Check if the tag exists
                    try:
                        tag = Tag.objects.filter(text=tag.text).first()
                        tags.append(tag)
                    except:
                        return HttpResponseBadRequest("Invalid tag", content_type="text/plain")

                # Check if the description already exists
                description = item.find("descricao").text
                if Quiz.objects.filter(description=description).exists():
                    return HttpResponseBadRequest("One or more quizzes already exist",
                                                  content_type="text/plain")

                try:
                    quiz = Quiz(
                        author=user,
                        question=description,
                        description=description,
                        name=description,
                        finished=True,
                        approved=True,
                    )
                    quiz.save()
                    quiz.tags.set(tags)
                except:
                    return HttpResponseBadRequest("Couldn't create quiz", content_type="text/plain")

                for answer in item.findall("./respostas/resposta"):

                    # If justification is not present, set it to empty string
                    if answer.find("justificacao").text is None:
                        justification = ""
                    else:
                        justification = answer.find("justificacao").text

                    try:
                        answer = QuizAnswer(
                            quiz=quiz,
                            text=answer.find("designacao").text,
                            correct=answer.find("valor_logico").text == "True",
                            justification=justification,
                        )
                        answer.save()
                    except:
                        return HttpResponseBadRequest("Couldn't create answer",
                                                      content_type="text/plain")
    except:
        return HttpResponseBadRequest("Invalid XML file format", content_type="text/plain")

    # Return JsonResponse with success message
    return JsonResponse({"message": "XML file loaded successfully"})


@api_view(['GET'])
def export_xml(request):
    # Get all quizzes
    data = Quiz.objects.all()
    if not data:
        return HttpResponseBadRequest('Quizzes not found', content_type="text/plain")

    for quiz in data:
        description = quiz.description
        answer_list = []
        answers = QuizAnswer.objects.filter(quiz=quiz)
        for answer in answers:
            answer_list.append(
                {
                    "text": answer.text,
                    "correct": answer.correct,
                    "justification": answer.justification,
                }
            )
        tag_list = []
        tags = quiz.tags.all()
        for tag in tags:
            tag_list.append(tag.text)


    # Create the XML file
    root = ET.Element("quizzes")
    tree = ET.ElementTree(root)
    root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    # Create the perguntas element
    perguntas = ET.SubElement(root, "perguntas")

    # Create the pergunta element for each quizz in data
    for quiz in data:
        pergunta = ET.SubElement(perguntas, "pergunta")

        tags = ET.SubElement(pergunta, "tags")
        # Create the tag element for each tag in the quiz
        for tag in quiz.tags.all():
            tag_element = ET.SubElement(tags, "tag")
            tag_element.text = tag.text

        descricao = ET.SubElement(pergunta, "descricao")
        descricao.text = quiz.description

        respostas = ET.SubElement(pergunta, "respostas")
        for answer in QuizAnswer.objects.filter(quiz=quiz):
            resposta = ET.SubElement(respostas, "resposta")
            
            designacao = ET.SubElement(resposta, "designacao")
            designacao.text = answer.text

            valor_logico = ET.SubElement(resposta, "valor_logico")
            valor_logico.text = str(answer.correct)

            justification = ET.SubElement(resposta, "justification")
            justification.text = answer.justification

    # Return xml file
    response = HttpResponse(content_type="text/xml")

    # Set the filename
    response["Content-Disposition"] = "attachment; filename=quiz.xml"

    # Write the XML file to the response
    tree.write(response, encoding="utf-8", xml_declaration=True)

    return response
