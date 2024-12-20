from faker import Faker
import random
faker = Faker("pt_BR") ##nomes brasileiros
##Avisos: 
## departamento nao eh um objeto! (ficou muito trabalho pra implementar no codigo ja existente, entao nao fiz :/)

## aluno_id possui 8 digitos 
## prof_id possui 7 digitos
## curso_id possui 6 digitos
## tcc_id possui 5 digitos
## dept_id possui 4 digitos
## disc_id possui 3 digitos

def montarID (qtIds,qtDigitos): ##monta IDs aleatorios
    Array = []
    digitomax = ""
    for x in range(qtDigitos):
        digitomax +="9"
    for x in range(qtIds):
        novoid = random.randint((10**(qtDigitos-1)),int(digitomax))
        while novoid in Array:
            novoid = random.randint((10**(qtDigitos-1)),int(digitomax))
        Array.append(novoid)
    return Array

def criarnome (): ##cria nomes unicos

    novonome = ""
    novo1onome = faker.unique.first_name()
    novo2onome = faker.unique.last_name()
    novonome += novo1onome
    novonome += " "
    novonome += novo2onome
    
    return novonome


anoinicio1 = 2015 ##ano minimo para historico
anofinal1 = 2019
anoinicio2 = 2020 
anofinal2 = 2024 ##ano maximo para historico



qtalunos = 50 ## qtde de alunos 
aluno_id = montarID(qtalunos,8) ##ids dos alunos


curso_nomes = ["Ciência da Computação","Engenharia Civil","Administração",] ##adicionar na mao 
## vv Relação entre cursos e disc
curso_disc = {"Ciência da Computação":["Cálculo","Engenharia de Software"],"Engenharia Civil":["Cálculo 2","Materia Engen."],"Administração":["Cálculo 3","Materia Admin."]} ##quais cursos tem quais disciplinas (adicionar na mão)

qtcurso = len(curso_nomes) ##qt de cursos
curso_id = montarID(qtcurso,6)## ids dos cursos

qtprof = 6 ## qtde de prof (TEM QUE SER IGUAL A QTDE DE DISC!!!) 
prof_id = montarID(qtprof,7) ##ids dos profs

tcc_nomes = ["Super Leonardo Bros.","Prédio Z","Reino-ministração"] ##adicionar na mao 
qttcc = len(tcc_nomes) ##qt de tccs
tcc_id = montarID(qttcc,5) ##ids dos tccs
integrantestcc = 2 ##qt de integrantes por tcc

dept_nomes = ["Exatas","Ciências","Humanas"] ##adicionar na mao
dept_cursos = {"Exatas":["Engenharia Civil"],"Ciências":["Ciência da Computação"],"Humanas":["Administração"]} ##adicionar na mao

qtdept = len(dept_cursos) ##qt de dept, tem que ser igual ou menor que quantidade de prof
dept_id = montarID(qtdept,4) ##ids dos dept   

disc_nomes = ["Cálculo","Cálculo 2","Cálculo 3","Engenharia de Software","Materia Engen.","Materia Admin."] ##para referencia!
qtdisc = len(disc_nomes) ##qt de disc
disc_id = montarID(qtdisc,3) ##ids das disc




class aula:## para montar historico (mesma qtde que profs)
    def __init__(self,disc_id,semestre,ano):
        self.disc_id = disc_id
        self.semestre = semestre
        self.ano = ano
        self.correcao = '{'
        self.correcao2 = '}'
    def __str__(self):
        return f"{self.correcao}{self.disc_id}\n{self.semestre}\n{self.ano}\n{self.correcao2}"
        

class aluno: ##para montar alunos
    def __init__(self,aluno_id,curso_id,aula,aula2=0):
        self.aluno_id = aluno_id ##id do aluno
        self.nome = criarnome() ##nome do aluno

        self.curso_id = curso_id
       
        self.aula = aula
        self.semestre = self.aula.semestre
        self.ano = self.aula.ano
        self.disc_id = self.aula.disc_id
        self.nota = random.randint(0,100)/10 ##nota aleatoria
        self.aula2 = aula2
        self.correcao = '{'
        self.correcao2 = '}'
        if self.aula2 != 0:
            self.semestre2 = self.aula2.semestre
            self.ano2 = self.aula2.ano
            self.disc_id2 = self.aula2.disc_id
            self.nota2 = random.randint(0,100)/10 
            
        
        


    def __str__(self): ##print basico
        return f"ID: {self.aluno_id}\nNome: {self.nome}\nCurso: {self.curso_id}\nDisc: {self.disc_id}\n"
    def insertDados(self): ##insert dos dados
        return f"db.aluno.insertOne({self.correcao}nome:\'{self.nome}\',aluno_id:\'{self.aluno_id}\',curso_id:\'{self.curso_id}\'{self.correcao2});\n"
    def historico(self): ##print do historico
        return f"Disc: {self.disc_id}\nNota: {self.nota}\nAno: {self.ano}\nSemestre: {self.semestre}\n"
    def insertHistorico(self): ##insert do historico
        if self.aula2 != 0:
            return f"db.historico_aluno.insertOne({self.correcao}aluno_id:\'{self.aluno_id}\',disc_id:\'{self.disc_id}\',curso_id:\'{self.curso_id}\',nota:{self.nota},semestre:{self.semestre},ano:{self.ano}{self.correcao2});\ndb.historico_aluno.insertOne({self.correcao}aluno_id:\'{self.aluno_id}\',disc_id:\'{self.disc_id2}\',curso_id:\'{self.curso_id}\',nota:{self.nota2},semestre:{self.semestre2},ano:{self.ano2}{self.correcao2});\n"
        else:
            return f"db.historico_aluno.insertOne({self.correcao}aluno_id:\'{self.aluno_id}\',disc_id:\'{self.disc_id}\',curso_id:\'{self.curso_id}\',nota:{self.nota},semestre:{self.semestre},ano:{self.ano}{self.correcao2});\n"
    

class professor: ##Refazer com ideias futuras
    def __init__(self,prof_id,dept_id,aula): ##aula sendo um objeto
        self.prof_id = prof_id ##id do prof
        self.nome = criarnome() ##nome do prof
        self.dept_id = dept_id ##nome do dept
        self.aula = aula
        self.disc_id = self.aula.disc_id
        self.semestre = self.aula.semestre
        self.ano = self.aula.ano
        self.correcao = '{'
        self.correcao2 = '}'

    def __str__(self):
        return f"ID: {self.prof_id}\nNome: {self.nome}\n"
    def insertDados(self):
        return f"db.professor.insertOne({self.correcao}nome:\'{self.nome}\',prof_id:\'{self.prof_id}\'{self.correcao2});\n"
    def insertHistorico(self):
        return f"db.historico_professor.insertOne({self.correcao}prof_id:\'{self.prof_id}\',disc_id:\'{self.disc_id}\',semestre:{self.semestre},ano:{self.ano}{self.correcao2});\n"
        
        
    
    
    
class tcc: ##por fazer
    def __init__(self,tcc_id,tcc_nome,prof_id,integrantes_id,curso_id):
        self.tcc_id = tcc_id ##id do tcc
        self.tcc_nome = tcc_nome ##nome do tcc
        self.prof_id = prof_id ##nome do prof responsavel
        self.integrantes_id = integrantes_id ##id dos integrantes (array)
        self.curso_id = curso_id ##id do curso
        self.correcao = '{'
        self.correcao2 = '}'
        
    def insertDados (self):
        return f"db.tcc.insertOne({self.correcao}nome:\'{self.tcc_nome}\',tcc_id:\'{self.tcc_id}\',curso_id:\'{self.curso_id}\',prof_id:\'{self.prof_id}\'{self.correcao2});\n"
    
    
class curso: ##possui curso_id,curso_nome e dept_id
    def __init__(self,curso_id,curso_nome):
        self.curso_id = curso_id ##id do curso
        self.curso_nome = curso_nome ##nome do curso
        self.correcao = '{'
        self.correcao2 = '}'
        
        pos = 0
        for x in dept_cursos: ##procura curso dentro de dept
            tododept = dept_cursos[x]
            if self.curso_nome in tododept:
                break
            pos +=1

        self.dept_id = dept_id[pos] ##id do dept
        self.discs_nomes = curso_disc[self.curso_nome]
        self.discs_ids = []
        for x in self.discs_nomes: ##cria uma lista com o id de todas as disc do curso
            for y in range(len(disc_nomes)):
                if x == disc_nomes[y]:
                    self.discs_ids.append(disc_id[y])
            
        

    def __str__ (self):
        return f"Dept_ID: {self.dept_id}\nCurso_ID: {self.curso_id}\nNome: {self.curso_nome}\n"
    def insertDados(self):
        return f"db.curso.insertOne({self.correcao}nome:\'{self.curso_nome}\',curso_id:\'{self.curso_id}\',dept_id:\'{self.dept_id}\'{self.correcao2});\n"
   
        
            

class departamento: ##possui dept_id, dept_nome,chefe_id,cursos do dept,discs do dept
    def __init__(self,dept_id,dept_nome,chefe_id):
        self.dept_id = dept_id
        self.dept_nome = dept_nome
        self.chefe_id = chefe_id
        self.cursos = dept_cursos[self.dept_nome] ##todos os cursos no dept
        self.discs = [] ##todas as disc no dept
        self.correcao = '{'
        self.correcao2 = '}'
        
        for x in range(len(self.cursos)): ##percorre para adicionar as disc
           discs_contidas = curso_disc[self.cursos[x]]
           for y in discs_contidas:
            self.discs.append(y)
            
    def insertDados(self):
        return f"db.departamento.insertOne({self.correcao}nome:\'{self.dept_nome}\',dept_id:\'{self.dept_id}\',chefe_id:\'{self.chefe_id}\'{self.correcao2});\n"

depts = []
for x in range(qtdept):
    depts.append(departamento(dept_id[x],dept_nomes[x],prof_id[x]))

aulas = []
for x in range(qtprof):
    if x < len(disc_id): ##criar historicos ate ter 1 para cada disc
        if x < 3:
            aulas.append(aula(disc_id[x],random.randint(1,2),random.randint(anoinicio1,anofinal1)))
        else:
            aulas.append(aula(disc_id[x],random.randint(1,2),random.randint(anoinicio2,anofinal2)))
    
    




alunos = [] ##todos os alunos
for x in range(qtalunos):
    if x%len(aulas) > 2:
        alunos.append(aluno(aluno_id[x],curso_id[x%qtcurso],aulas[x%len(aulas)-3],aulas[x%len(aulas)]))
    else:
        alunos.append(aluno(aluno_id[x],curso_id[x%qtcurso],aulas[x%len(aulas)]))
    ##print(alunos[x]) ##print de teste
    ##print(alunos[x].historico()) ##print de teste 

profs = [] ##todos os prof
for x in range(qtprof):
    if x < qtcurso:
        profs.append(professor(prof_id[x],dept_nomes[x],aulas[x])) ##forca os primeiros a obrigatoriamente serem parte do dept que sao chefes
    else:
        profs.append(professor(prof_id[x],dept_nomes[random.randint(0,qtdept-1)],aulas[x])) ##adiciona objetos professor
    ##print(profs[x]) ##print de teste
    ##print(profs[x].insertHistorico()) ##print de teste


cursos = [] ##todos os cursos
for x in range(qtcurso):
    cursos.append(curso(curso_id[x],curso_nomes[x]))
    ##print(cursos[x]) ##print de teste

tccs = []
for x in range(qttcc):
    alunosintegrantes = []

    for y in range(integrantestcc):
        for c in alunos:
            if c.curso_id == curso_id[x]:
                alunosintegrantes.append(c.aluno_id)
                
    tccs.append(tcc(tcc_id[x],tcc_nomes[x],prof_id[x],alunosintegrantes,curso_id[x]))


arquivo = open("dadosInsert.txt","w",encoding="utf-8") ##arquivo para depois usar no sql
 ## insercao de dados no arquivo
for x in range(qtalunos): ##insere dados dos alunos e seus historicos
    arquivo.write(alunos[x].insertDados())
    arquivo.write(alunos[x].insertHistorico())
 
for x in range(qtcurso): ##insere dados dos cursos
    arquivo.write(cursos[x].insertDados())

for x in range(qtdept): ##insere dados dos dept
    arquivo.write(depts[x].insertDados())

for x in range(qtprof): ##insere dados dos profs
    arquivo.write(profs[x].insertDados())
    arquivo.write(profs[x].insertHistorico())



for x in range(qtdisc): ##insere dados da disc ( nao usa orientacao objeto :( )
    for y in depts:
        if disc_nomes[x] in y.discs:
            idprocurado = y.dept_id
    arquivo.write("db.disciplina.insertOne({nome:\'%s\',disc_id:\'%s\',dept_id:\'%s\'});\n" %(disc_nomes[x],disc_id[x],idprocurado))
    
   
for x in cursos: ##insere dados da matriz_curricular
    sem = 1
    for y in x.discs_ids:
        arquivo.write("db.matriz_curricular.insertOne({curso_id:\'%s\',disc_id:\'%s\',semestre:%s});\n" %(y,x.curso_id,sem))
        sem +=1

for x in tccs: ##insere dados dos tccs
    
    arquivo.write(x.insertDados())
    for y in range(integrantestcc):
        arquivo.write("db.grupo_tcc.insertOne({tcc_id:\'%s\',aluno_id:\'%s\'});\n" %(x.tcc_id,x.integrantes_id[y]))

for x in alunos: ##insere dados dos graduados
    if x.aula2 !=0:
        if x.nota >= 5 and x.nota2>=5:
            ##print(x.aluno_id,x.nome,x.curso_id) ##print de teste
            arquivo.write("db.graduado.insertOne({aluno_id:\'%s\',nome:\'%s\',curso_id:\'%s\',semestre:%s,ano:%s});\n"%(x.aluno_id,x.nome,x.curso_id,x.semestre2,x.ano2)) ##para ficar facil de saber quem graduou


arquivo.close()
