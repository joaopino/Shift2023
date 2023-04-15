import traceback

from django.contrib.auth.models import User as AuthUser
from django.db import DatabaseError, IntegrityError
from moelasware.models import *


# RUN WITH
#   python manage.py shell < populate_db.py


SAVE = False


def save(*obj):
    if SAVE:
        for o in obj:
            o.save()


# Quizzes
print("Creating users")
try:
    manel = AuthUser.objects.create_user("manel", "manel@sapo.pt", "1234")
except IntegrityError:
    print("Manel already exists")
    pass

try:
    john = AuthUser.objects.create_user("john", "reese@themachine.com", "harold")
except IntegrityError:
    print("John already exists")
    pass
try:
    sergio = AuthUser.objects.create_user("sergio42", "sergio@hotmail.com", "superior-brother")
except IntegrityError:
    print("Sergio already exists")
    pass

try:
    joao = AuthUser.objects.create_user(username="Joao",
		                                email="joao@hotmail.com",
		                                password="joao12345")
except IntegrityError:
    print("João already exists")
    pass

try:
    andre = AuthUser.objects.create_user(username="Andre",
		                                email="andre123@gmail.com",
		                                password="andre123andre")
except IntegrityError:
    print("André already exists")
    pass


try:
    luis = AuthUser.objects.create_user(username="Luis",
		                                email="lui_pedro@sapo.pt",
		                                password="luis_123")
except IntegrityError:
    print("Luis already exists")
    pass


try:
    manel = AuthUser.objects.get(username="manel")
    john = AuthUser.objects.get(username="john")
    sergio = AuthUser.objects.get(username="sergio42")

    joao= AuthUser.objects.get(username="Joao")
    andre = AuthUser.objects.get(username="Andre")
    luis = AuthUser.objects.get(username="Luis")

    User.objects.bulk_create(
        [
            User(user=manel), #0
            User(user=john), #1
            User(user=sergio), #2
 
            User(user=joao), #3
            User(user=andre), #4
            User(user=luis), #5
        ]
    )
    print("Creating tags")
    tags = Tag.objects.bulk_create(
        [
            Tag(text="Math"), #0 
            Tag(text="Travel"), #1
            Tag(text="Culture"), #2
            Tag(text="REQ"), #3
            Tag(text="PM"), #4
            Tag(text="A&D"), #5
            Tag(text="IMP"), #6
            Tag(text="TST"), #7
            Tag(text="V&V"), #8
            Tag(text="DEP"), #9
            Tag(text="CI"), #10
            Tag(text="PRC"), #11
            Tag(text="PPL"), #12
            Tag(text="CCM"), #13
            Tag(text="RSK"), #14
        ]
    )
    print("Creating quizzes")
    quizzes = Quiz.objects.bulk_create(
        [
            #0
            Quiz(
                author=User.objects.get(user=manel),
                question="Question1",
                description="description1",
                name="Quiz1",
                finished = True,
                approved = True,
            ),
            #1
            Quiz(
                author=User.objects.get(user=manel),
                question="Baby is ____?",
                description="How would you describe baby?",
                name="Quiz2",
                finished = True,
                approved = True,
            ),
            #2
            Quiz(
                author=User.objects.get(user=manel),
                question="What is the best fruit?",
                description="objectively, what fruit is the best ever",
                name="Quiz3",
                finished = True,
                approved = False,
            ),
            #3
            Quiz(
                author=User.objects.get(user=manel),
                question="A B C _ ?",
                description="do you know letters?",
                name="Quiz4",
                finished = True,
                approved = True,
            ),
            #4
            Quiz(
                author=User.objects.get(user=manel),
                question="What is 9 + 10?",
                description="math is easy",
                name="Quiz5",
                finished = True,
                approved = False,
            ),
            #5
            Quiz(
                author=User.objects.get(user=manel),
                question="How many Fast and Furious Movies are there?",
                description="too many?",
                name="Quiz6",
                finished = True,
                approved = True,
            ),
            #6
            Quiz(
                author=User.objects.get(user=manel),
                question="When was Minecraft 1.0 released?",
                description="too many?",
                name="Quiz7",
                finished = True,
                approved = True,
            ),
            #7
            Quiz(
                author=User.objects.get(user=sergio),
                question="How many books has Operah Winfrey written?",
                description="how many?",
                name="Quiz8",
                finished = False,
                approved = False,
            ),
            #8
            Quiz(
                author=User.objects.get(user=sergio),
                question="Which of these animals does NOT make milk?",
                description="nature be wild",
                name="Quiz9",
                finished = True,
                approved = True,
            ),
            #9
            Quiz(
                author=User.objects.get(user=sergio),
                question="What makes plants green?",
                description="nature be wild",
                name="Quiz10",
                finished = True,
                approved = True,
            ),
            #10
            Quiz(
                author=User.objects.get(user=sergio),
                question="Who voiced batman?",
                description="RIP :(",
                name="Quiz11",
                finished = True,
                approved = True,
            ),
            #11
            Quiz(
                author=User.objects.get(user=sergio),
                question="What are the LOST numbers?",
                description="Great 4 seasons.",
                name="Quiz12",
                finished = True,
                approved = True,
            ),
            #12
            Quiz(
                author=User.objects.get(user=sergio),
                question="How many cats exist in the world?",
                description="Never enough",
                name="Quiz13",
                finished = True,
                approved = True,
            ),
            #13
            Quiz(
                author=User.objects.get(user=sergio),
                question="O que é húmus?",
                description="Fun",
                name="Quiz14",
                finished = True,
                approved = False,
            ),
            #14
            Quiz(
                author=User.objects.get(user=sergio),
                question="Quantos modelos de iPhone existem?",
                description="They're all the same",
                name="Quiz15",
                finished = False,
                approved = False,
            ),
            #15
            Quiz( 
                author=User.objects.get(user=joao),
		        question="Qual das seguintes áreas é que está diretamente ligada ao peopleware?",
		        description="Peopleware são um grupo de pessoas que trabalham diretamente, ou indiretamente, com uma determinada área.",
		        name="Área de Peopleware",
                finished = True,
                approved = True,
            ),
            #16
            Quiz( 
                author=User.objects.get(user=joao),
		        question="Os requisitos não funcionais podem ser divididos em:",
                description="Requisitos não funcionais são os requisitos relacionados com o uso da aplicação em termos de desempenho, usabilidade, confiabilidade, segurança, disponibilidade, manutenção e tecnologias envolvidas. Estes requisitos dizem respeito a como as funcionalidades serão entregues ao usuário do software.",
                name="Requisitos não funcionais",
                finished = True,
                approved = True,
            ),
            #17
            Quiz( 
                author=User.objects.get(user=john),
		        question="Qual das seguintes, não pertence às fases do ciclo de vida do software?",
                description="O ciclo de vida do software, refere-se a uma metodologia com processos definidos para a criação de software de alta qualidade.",
                name="Ciclo de vida do software",
                finished = True,
                approved = True,
            ),
            #18
            Quiz( 
                author=User.objects.get(user=john),
		        question="Qual das seguintes, não é uma atividade do processo de manutenção de um produto?",
                description="A manutenção de software é um processo que faz parte do ciclo de qualquer projeto de desenvolvimento de produtos. Este processo pode ser feito com vários propósitos (otimização, ajustes, requisições do cliente, etc) e ocorre após a entrega do produto ou, às vezes, durante a sua concepção.",
                name="Processo de manutenção",
                finished = True,
                approved = False,
            ),
            #19
            Quiz( 
                author=User.objects.get(user=sergio),
		        question="Qual das seguintes, não caracteriza o modelo em cascata?",
                description="O modelo cascata, também conhecido como processo Waterfall, é uma metodologia de desenvolvimento de software surgida na década de 1970. A sua principal característica é a divisão das tarefas em etapas predeterminadas.",
                name="Modelo em cascata",
                finished = False,
                approved = False,
            ),
            #20
            Quiz( 
                author=User.objects.get(user=sergio),
		        question="A validação dos requesitos:",
                description="Normalmente, a validação dos requesitos é usada para identificar quaisquer erros nas fases iniciais do ciclo de desenvolvimento. Se esses erros não forem detectados a tempo, eles podem aumentar excessivamente o trabalho.",
                name="Validação dos requesitos",
                finished = True,
                approved = True,
            ),
            #21
            Quiz( 
                author=User.objects.get(user=sergio),
		        question="Qual das seguintes, não é uma atividade do processo de planeamento do projeto?",
                description="O planeamento dos projetos é a parte que visa definir o escopo do mesmo, suas atividades posteriores e comunicar estas definições ao resto das partes interessadas. Considerada a etapa primordial, este planeamento é decisivo na qualidade de todo o ciclo de vida do projeto.",
                name="Processo de planeamento do projeto",
                finished = True,
                approved = True,
            ),
        ]
    )

    quizzes[0].tags.set([tags[2]])
    quizzes[1].tags.set([tags[5]])
    quizzes[2].tags.set([tags[6]])
    quizzes[3].tags.set([tags[4]])
    quizzes[4].tags.set([tags[0]])
    quizzes[5].tags.set([tags[2]])
    quizzes[6].tags.set([tags[7]])

    quizzes[7].tags.set([tags[12]])
    quizzes[8].tags.set([tags[12]])
    quizzes[9].tags.set([tags[8]])
    quizzes[10].tags.set([tags[13]])
    quizzes[11].tags.set([tags[14]])
    quizzes[12].tags.set([tags[1]])
    quizzes[13].tags.set([tags[2]])
    quizzes[14].tags.set([tags[0]])

    quizzes[15].tags.set([tags[11]])
    quizzes[16].tags.set([tags[3]])
    quizzes[17].tags.set([tags[7]])
    quizzes[18].tags.set([tags[13]])
    quizzes[19].tags.set([tags[11]])
    quizzes[20].tags.set([tags[3]])
    quizzes[21].tags.set([tags[4]])

    

    print("Creating answers")
    answers = QuizAnswer.objects.bulk_create(
        [
            QuizAnswer(
                quiz=quizzes[0],
                text="answer1",
                correct=False,
                justification="justification",
            ),
            QuizAnswer(
                quiz=quizzes[0],
                text="answer2",
                correct=False,
                justification="justification",
            ),
            QuizAnswer(
                quiz=quizzes[0],
                text="answer3",
                correct=True,
                justification="justification",
            ),
            QuizAnswer(
                quiz=quizzes[0],
                text="answer4",
                correct=False,
                justification="justification",
            ),
            QuizAnswer(
                quiz=quizzes[1],
                text="ugly",
                correct=False,
                justification="justification",
            ),
            QuizAnswer(
                quiz=quizzes[1],
                text="old cat",
                correct=False,
                justification="justification",
            ),
            QuizAnswer(
                quiz=quizzes[1],
                text="bad",
                correct=False,
                justification="justification",
            ),
            QuizAnswer(
                quiz=quizzes[1],
                text="BABY",
                correct=True,
                justification="justification",
            ),

            QuizAnswer(
                quiz=quizzes[2],
                text="apple",
                correct=True,
                justification="is best",
            ),
            QuizAnswer(
                quiz=quizzes[2],
                text="grapes",
                correct=False,
                justification="just ok",
            ),
            QuizAnswer(
                quiz=quizzes[2],
                text="tomato",
                correct=False,
                justification="u weirdo",
            ),
            QuizAnswer(
                quiz=quizzes[2],
                text="banana",
                correct=False,
                justification="disgusting",
            ),

            QuizAnswer(
                quiz=quizzes[3],
                text="69",
                correct=False,
                justification="justification",
            ),
            QuizAnswer(
                quiz=quizzes[3],
                text="D",
                correct=False,
                justification="justification",
            ),
            QuizAnswer(
                quiz=quizzes[3],
                text="deeeeezzzz nuutsss",
                correct=True,
                justification="justification",
            ),
            QuizAnswer(
                quiz=quizzes[3],
                text="green",
                correct=False,
                justification="justification",
            ),

            QuizAnswer(
                quiz=quizzes[4],
                text="69",
                correct=False,
                justification="funny",
            ),
            QuizAnswer(
                quiz=quizzes[4],
                text="19",
                correct=False,
                justification="u smort",
            ),
            QuizAnswer(
                quiz=quizzes[4],
                text="21?",
                correct=True,
                justification="memes",
            ),
            QuizAnswer(
                quiz=quizzes[4],
                text="2",
                correct=False,
                justification="looks right",
            ),

            QuizAnswer(
                quiz=quizzes[5],
                text="69",
                correct=False,
                justification="maybe someday",
            ),
            QuizAnswer(
                quiz=quizzes[5],
                text="10",
                correct=True,
                justification="u smort",
            ),
            QuizAnswer(
                quiz=quizzes[5],
                text="2",
                correct=False,
                justification="memes",
            ),
            QuizAnswer(
                quiz=quizzes[5],
                text="7",
                correct=False,
                justification="no",
            ),

            QuizAnswer(
                quiz=quizzes[6],
                text="2014",
                correct=False,
                justification="Herobrine",
            ),
            QuizAnswer(
                quiz=quizzes[6],
                text="10 A.C.",
                correct=False,
                justification="who's to say??",
            ),
            QuizAnswer(
                quiz=quizzes[5],
                text="69",
                correct=False,
                justification="why??",
            ),
            QuizAnswer(
                quiz=quizzes[5],
                text="2011",
                correct=True,
                justification="great year",
            ),
            QuizAnswer(
                quiz=quizzes[7],
                text="2",
                correct=False,
                justification="No",
            ),
            QuizAnswer(
                quiz=quizzes[7],
                text="10",
                correct=False,
                justification="No",
            ),
            QuizAnswer(
                quiz=quizzes[7],
                text="69",
                correct=False,
                justification="No",
            ),
            QuizAnswer(
                quiz=quizzes[7],
                text="0",
                correct=False,
                justification="at one point it was true",
            ),
            QuizAnswer(
                quiz=quizzes[7],
                text="5",
                correct=True,
                justification="Yes",
            ),
            QuizAnswer(
                quiz=quizzes[7],
                text="6",
                correct=False,
                justification="No",
            ),

            QuizAnswer(
                quiz=quizzes[8],
                text="Cow",
                correct=False,
                justification="No",
            ),
            QuizAnswer(
                quiz=quizzes[8],
                text="Platypus",
                correct=False,
                justification="No",
            ),
            QuizAnswer(
                quiz=quizzes[8],
                text="Snail",
                correct=True,
                justification="That would be CRAZY!",
            ),
            QuizAnswer(
                quiz=quizzes[8],
                text="Pidgeon",
                correct=False,
                justification="at one point it was true",
            ),
            QuizAnswer(
                quiz=quizzes[8],
                text="Dolphin",
                correct=False,
                justification="Yes",
            ),
            QuizAnswer(
                quiz=quizzes[8],
                text="Cat",
                correct=False,
                justification="No",
            ),

            QuizAnswer(
                quiz=quizzes[9],
                text="Cow",
                correct=False,
                justification="No",
            ),
            QuizAnswer(
                quiz=quizzes[9],
                text="Light Yagamy",
                correct=False,
                justification="No",
            ),
            QuizAnswer(
                quiz=quizzes[9],
                text="Swadloon",
                correct=False,
                justification="No",
            ),
            QuizAnswer(
                quiz=quizzes[9],
                text="Green+",
                correct=False,
                justification="No",
            ),
            QuizAnswer(
                quiz=quizzes[9],
                text="Leafeon",
                correct=False,
                justification="Yes",
            ),
            QuizAnswer(
                quiz=quizzes[9],
                text="Chlorophyll",
                correct=True,
                justification="Fancy word",
            ),

            QuizAnswer(
                quiz=quizzes[10],
                text="Kevin Conroy",
                correct=True,
                justification="RIP",
            ),
            QuizAnswer(
                quiz=quizzes[10],
                text="Mark Hamill",
                correct=False,
                justification="No",
            ),
            QuizAnswer(
                quiz=quizzes[10],
                text="Christian Bale",
                correct=False,
                justification="No",
            ),
            QuizAnswer(
                quiz=quizzes[10],
                text="Pete Davidson",
                correct=False,
                justification="No",
            ),
            QuizAnswer(
                quiz=quizzes[10],
                text="Mathew Mercer",
                correct=False,
                justification="No",
            ),
            QuizAnswer(
                quiz=quizzes[10],
                text="Matt Daemon",
                correct=False,
                justification="No",
            ),

            QuizAnswer(
                quiz=quizzes[11],
                text="4 2 15 16 24 42",
                correct=False,
                justification="No",
            ),
            QuizAnswer(
                quiz=quizzes[11],
                text="1 2 13 14 25 42",
                correct=False,
                justification="No",
            ),
            QuizAnswer(
                quiz=quizzes[11],
                text="4 8 15 16 23 42",
                correct=True,
                justification="4 8 15 16 23 42",
            ),
            QuizAnswer(
                quiz=quizzes[11],
                text="1 8 13 16 25 41",
                correct=False,
                justification="No",
            ),
            QuizAnswer(
                quiz=quizzes[11],
                text="4 2 15 14 25 42",
                correct=False,
                justification="No",
            ),
            QuizAnswer(
                quiz=quizzes[11],
                text="1 8 15 13 23 45",
                correct=False,
                justification="No",
            ),

            QuizAnswer(
                quiz=quizzes[12],
                text="420 million",
                correct=False,
                justification="No",
            ),
            QuizAnswer(
                quiz=quizzes[12],
                text="600 million",
                correct=True,
                justification="Miau",
            ),
            QuizAnswer(
                quiz=quizzes[12],
                text="100 million",
                correct=False,
                justification="No",
            ),
            QuizAnswer(
                quiz=quizzes[12],
                text="4",
                correct=False,
                justification="No",
            ),
            QuizAnswer(
                quiz=quizzes[12],
                text="500 million",
                correct=False,
                justification="No",
            ),
            QuizAnswer(
                quiz=quizzes[12],
                text="300 million",
                correct=False,
                justification="No",
            ),

            QuizAnswer(
                quiz=quizzes[13],
                text="Uma aldeia na baía de Santarém",
                correct=False,
                justification="No",
            ),
            QuizAnswer(
                quiz=quizzes[13],
                text="Uma espécie de animal",
                correct=False,
                justification="No",
            ),
            QuizAnswer(
                quiz=quizzes[13],
                text="Uma espécie de planta",
                correct=False,
                justification="No",
            ),
            QuizAnswer(
                quiz=quizzes[13],
                text="Comida de cão",
                correct=False,
                justification="No",
            ),
            QuizAnswer(
                quiz=quizzes[13],
                text="Uma espécie de cocó",
                correct=True,
                justification="Very funny",
            ),
            QuizAnswer(
                quiz=quizzes[13],
                text="Um monte de minhocas",
                correct=False,
                justification="No",
            ),

            QuizAnswer(
                quiz=quizzes[14],
                text="3",
                correct=False,
                justification="No",
            ),
            QuizAnswer(
                quiz=quizzes[14],
                text="34",
                correct=True,
                justification="Are they all the same?",
            ),
            QuizAnswer(
                quiz=quizzes[14],
                text="21",
                correct=False,
                justification="No",
            ),
            QuizAnswer(
                quiz=quizzes[14],
                text="42",
                correct=False,
                justification="No",
            ),
            QuizAnswer(
                quiz=quizzes[14],
                text="10",
                correct=False,
                justification="No",
            ),
            QuizAnswer(
                quiz=quizzes[14],
                text="17",
                correct=False,
                justification="No",
            ),

            QuizAnswer(
                quiz=quizzes[15],
                text="Saúde",
                correct=False,
                justification="O peopleware está relacionado diretamente com a área da tecnologia.",
            ),
            QuizAnswer(
                quiz=quizzes[15],
                text="Tecnologia da informação",
                correct=True,
                justification="O peopleware é a parte humana que se utiliza das diversas funcionalidades dos sistemas computacionais, seja este usuário um analista de sistema ou, até mesmo, um simples cliente que faz uma consulta em um caixa eletrônico da Rede Bancária.",
            ),
            QuizAnswer(
                quiz=quizzes[15],
                text="Música",
                correct=False,
                justification="O peopleware está relacionado diretamente com a área da tecnologia.",
            ),
            QuizAnswer(
                quiz=quizzes[15],
                text="Psicologia",
                correct=False,
                justification="O peopleware está relacionado diretamente com a área da tecnologia.",
            ),

            QuizAnswer(
                quiz=quizzes[16],
                text="Requisitos do produto, requisitos legislativos e requisitos de eficiência",
                correct=False,
                justification="Os requisitos de segurança e legislativos não são requisitos não funcionais.",
            ),
            QuizAnswer(
                quiz=quizzes[16],
                text="Requisitos de segurança, requisitos do produto e requisitos externos",
                correct=False,
                justification="Os requisitos de segurança não são requisitos não funcionais.",
            ),
            QuizAnswer(
                quiz=quizzes[16],
                text="Requisitos de segurança, requisitos do produto e requisitos externos",
                correct=False,
                justification="Os requisitos de segurança não são requisitos não funcionais.",
            ),
            QuizAnswer(
                quiz=quizzes[16],
                text="Requisitos do produto, requisitos organizacionais e requisitos externos",
                correct=True,
                justification="Os requisitos do produto especificam o comportamento deste, os requisitos organizacionais são decorrentes de políticas e procedimentos corporativos e os requisitos externos são decorrentes de fatores externos ao sistema e ao processo de desenvolvimento.",
            ),

            QuizAnswer(
                quiz=quizzes[17],
                text="Gestão de projetos",
                correct=True,
                justification="A gestão de projetos não pertence ao ciclo de vida do software. Este tem o seu ciclo de vida tendo as 4 seguintes etapas: iniciação, planeamento, execução e encerramento.",
            ),
            QuizAnswer(
                quiz=quizzes[17],
                text="Design",
                correct=False,
                justification="Esta fase permite transformar os requisitos do usuário numa alguma forma mais adequada, o que ajuda o programador na codificação e implementação do software.",
            ),
            QuizAnswer(
                quiz=quizzes[17],
                text="Testar",
                correct=False,
                justification="A fase de testar é o que permite aos devolopers verificar se o que fizeram está a funcionar como devia, de acordo com os requisitos.",
            ),
            QuizAnswer(
                quiz=quizzes[17],
                text="Manutenção",
                correct=False,
                justification="A fase de manutençao é o que permite melhorar o sistema sempre que uma falha for encontrada.",
            ),

            QuizAnswer(
                quiz=quizzes[18],
                text="Análise do impacto",
                correct=False,
                justification="Quando o produto é lançado, também é necessário saber o impacto que teve na sociedade, para futuras alterações no mesmo.",
            ),
            QuizAnswer(
                quiz=quizzes[18],
                text="Mudanças na implementação",
                correct=False,
                justification="Sejam mudanças para corrigir erros ou novas funcionalidades, esta atividade é o centro do processo de manutenção do produto.",
            ),
            QuizAnswer(
                quiz=quizzes[18],
                text="Planeamento de uma nova versao do sistema",
                correct=False,
                justification="Planear uma nova versão é uma atividade pois sempre que ocorra uma alteração no produto final, seja esta pequena ou grande, irá existir uma nova versão do mesmo.",
            ),
            QuizAnswer(
                quiz=quizzes[18],
                text="Gestão de qualidade",
                correct=True,
                justification="A gestão de qualidade não pertence ao processo de manutenção do produto. Esta atividade apenas permite disputar a concorrência com as empresas do ramo.",
            ),

            QuizAnswer(
                quiz=quizzes[19],
                text="É adequado para projetos com requesitos estáveis",
                correct=False,
                justification="Caso os requisitos não sejam estáveis, ou seja, são alterados ou modificados com frequência, todas as etapas teriam de ser executadas de novo e sequencialmente, algo que não é ideal, visto que, iria ocupar demasiado tempo.",
            ),
            QuizAnswer(
                quiz=quizzes[19],
                text="É caracterizado por um conjuto de metas e prazos de entregas claramente definidos",
                correct=False,
                justification="Neste modelo, existem prazos de entregas e metas definidas para saber como o progresso do projeto, visto que, todas as tarefas devem ser cumpridas num certo prazo. Isto permite também saber quando o projeto deve estar finalizado.",
            ),
            QuizAnswer(
                quiz=quizzes[19],
                text="Feedback contínuo do cliente",
                correct=False,
                justification="Este modelo não tem um feedback contínuo do cliente, visto que, a interação dele com a equipa de desenvolvimento geralmente acontece no início e no fim do projeto. Quando o projeto está concluído, a primeira versão executável do software é entregue ao cliente para que ele opine sobre esta. Caso haja algum problema, a equipa terá que reiniciar o modelo em cascata para realizar as mudanças necessárias.",
            ),
            QuizAnswer(
                quiz=quizzes[19],
                text="É um modelo sequencial para desenvolvimento de software",
                correct=True,
                justification="As etapas são executadas de forma sequencial, ou seja, é preciso finalizar todas as tarefas de uma etapa para que seja possível passar para a seguinte. Ao cumprir todas as etapas, o resultado será um produto de software funcional, pronto para ser entregue ao cliente.",
            ),

            QuizAnswer(
                quiz=quizzes[20],
                text="é o processo que verifica a exatidão e a integridade dos requesitos",
                correct=True,
                justification="A validação garante precisão e clareza nos dados, mitigando quaisquer defeitos nos requisitos coletados. Sem validação, há um alto risco de dados imprecisos que resultariam em resultados imprecisos. Assim, é preciso verificar a exatidão e a integridade dos mesmos.",
            ),
            QuizAnswer(
                quiz=quizzes[20],
                text="faz parte do estudo de viabilidade",
                correct=False,
                justification="O estudo de viabilidade é a análise de viabilidade ou uma medida do produto de software em termos de quanto o desenvolvimento do produto será benéfico para a organização do ponto de vista prático, não fazendo parte da validação dos requesitos.",
            ),
            QuizAnswer(
                quiz=quizzes[20],
                text="é realizada por meio de testes unitários e de integração",
                correct=False,
                justification="Os testes unitários e de integração só são executadas na fase de testes do ciclo de vida do software.",
            ),
            QuizAnswer(
                quiz=quizzes[20],
                text="garante que o cliente aceite o software",
                correct=False,
                justification="Nao se trata disto, trata-se de verificar se estamos a construir o sistema como o cliente deseja.",
            ),

            QuizAnswer(
                quiz=quizzes[21],
                text="Revisão do produto",
                correct=True,
                justification="Esta atividade não pertence ao processo de planeamento do projeto.",
            ),
            QuizAnswer(
                quiz=quizzes[21],
                text="Revisao do progresso do projeto",
                correct=False,
                justification="Esta atividade é essencial, visto que, é o que permite verificar o estado do projeto.",
            ),
            QuizAnswer(
                quiz=quizzes[21],
                text="Definir metas e prazos entregas do projeto",
                correct=False,
                justification="Definir metas e prazos entregas permite saber como o projeto vai numa certa data, visto que, todas as tarefas devem ser cumpridas num certo prazo. Isto permite também saber quando o projeto deve estar finalizado.",
            ),
            QuizAnswer(
                quiz=quizzes[21],
                text="Elaborar o cronograma do projeto",
                correct=False,
                justification="Ter um cronograma do projeto ajuda a organizar todo o projeto, e também, ajuda a saber quando pudemos mostrar o produto a funcionar ao cliente, para recebermos feedback.",
            ),
        ]
    )

    print("Creating tests")

    tests = Test.objects.bulk_create(
        [
            Test(author=User.objects.get(user=manel), name="Nature"),
            Test(author=User.objects.get(user=john), name="Media"),
            Test(author=User.objects.get(user=manel), name="Memes"),
            Test(author=User.objects.get(user=sergio), name="Random"),
        ]
    )
    tests[0].quizzes.set([quizzes[8], quizzes[9], quizzes[12]])
    tests[1].quizzes.set([quizzes[5], quizzes[10], quizzes[11]])
    tests[2].quizzes.set([quizzes[1], quizzes[3], quizzes[13]])
    tests[3].quizzes.set([quizzes[1], quizzes[8], quizzes[13], quizzes[9], quizzes[12], quizzes[10]])

    # Submissions
    print("Creating submissions")
    submissions = Submission.objects.bulk_create(
        [
            Submission(test=tests[0], submitter=User.objects.get(user=john)),
            Submission(test=tests[1], submitter=User.objects.get(user=john)),
        ]
    )

    submission_answers = SubmissionAnswer.objects.bulk_create(
        [
            SubmissionAnswer(submission=submissions[0], answer=answers[0]),
            SubmissionAnswer(submission=submissions[0], answer=answers[1]),
            SubmissionAnswer(submission=submissions[1], answer=answers[0]),
            SubmissionAnswer(submission=submissions[1], answer=answers[2]),
        ]
    )

    # Reviews
    print("Creating reviews")
    reviews = Review.objects.bulk_create(
        [
            Review(
                reviewer=User.objects.get(user=manel),
                quiz=quizzes[0],
                accepted=False,
                comment="comment",
            ),
            Review(
                reviewer=User.objects.get(user=manel),
                quiz=quizzes[1],
                accepted=False,
                comment="comment",
            ),
            Review(
                reviewer=User.objects.get(user=manel),
                quiz=quizzes[2],
                accepted=False,
                comment="comment",
            ),

        ]
    )

except DatabaseError:
    traceback.print_exc()
    print("Oops")
