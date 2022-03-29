from Noticias import Noticias
from .lista_estados import *

lista_noticias = [
    #       id  data postagem titulo        previa
    Noticias(0, "17/02/2004", "Lorem 00",
             "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Optio nostrum minima id explicabo facere "
             "atque? Cupiditate nam natus minima iusto.",
             "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Optio nostrum minima id explicabo facere "
             "atque? Cupiditate nam natus minima iusto." * 10),

    Noticias(1, "23/03/2005", "Lorem 01",
             "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Optio nostrum minima id explicabo facere "
             "atque? Cupiditate nam natus minima iusto.",
             "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Optio nostrum minima id explicabo facere "
             "atque? Cupiditate nam natus minima iusto." * 7),

    Noticias(2, "21/05/2006", "Lorem 02",
             "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Optio nostrum minima id explicabo facere "
             "atque? Cupiditate nam natus minima iusto.",
             "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Optio nostrum minima id explicabo facere "
             "atque? Cupiditate nam natus minima iusto." * 5),

    Noticias(3, "22/05/2006", "Lorem 03",
             "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Optio nostrum minima id explicabo facere "
             "atque? Cupiditate nam natus minima iusto.",
             "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Optio nostrum minima id explicabo facere "
             "atque? Cupiditate nam natus minima iusto." * 17, "Pará"),
    
    Noticias(4, 
             "14/03/2022", 
             "Mesmo com vazante, três cidades do AC seguem com nível dos rios acima da cota de transbordo",
             "Estão com nível dos rios acima da cota de transbordo a capital acreana, Rio Branco, Sena Madureira, Porto Acre e Cruzeiro do Sul.",
             "Alguns rios que estão acima da cota de transbordo apresentaram vazante nesta segunda-feira (28). Entre eles estão o Rio Acre, em Rio Branco, Iaco, em Sena Madureira, e Juruá, em Cruzeiro do Sul, que mesmo assim continuam acima da cota de transbordo, de acordo com o informativo diário da Defesa Civil Estadual.Além destas três cidades, Porto Acre foi o único município onde o Rio Acre apresentou aumento no nível das águas que chegou à cota de 13,22 metros nesta segunda e está a 72 centímetros acima da cota de transbordo, que é de 12,50 metros. Porém, nenhuma família foi removida. Os efeitos da cheia fizeram o governador Gladson Cameli decretar situação de emergência em Feijó, Tarauacá, Sena Madureira, Santa Rosa do Purus, Jordão e Cruzeiro do Sul. O decreto foi publicado no Diário Oficial do Estado (DOE) e tem validade de 90 dias. Feijó e Tarauacá, cidades onde os rio transbordaram na semana passada, os rios Envira (11,70 metros) e Tarauacá (9 metros) voltaram a subir nesta segunda, mas estão abaixo da cota de transbordo, 12 metros e 9,50 metros, respectivamente.", 
             estado_acre),
    
    Noticias(5, 
             "28/03/2022", 
             "Alagoas confirma 47 novos casos e mais 4 mortes por Covid",
             "Estado tem 1.327 casos suspeitos do coronavírus. Total de óbitos chegou a 6.873.",
             "Alagoas registrou 47 novos casos e mais quatro mortes por Covid nesta segunda-feira (28), de acordo com a Secretaria de Estado da Saúde (Sesau). No último domingo (27), foi a primeira vez desde o início da pandemia, em março de 2020, que o estado não registrou casos e óbitos por Covid.O total acumulado desde o início da pandemia é 296.019 casos conhecidos e 6.873 mortes. Do total de pessoas diagnosticadas com infecção pelo coronavírus, 288.709 estão recuperadas.O estado também acumula 1.327 casos suspeitos, à espera de resultado de exame.Dos 284 leitos exclusivos para Covid e influenza, 29 estavam ocupados até as 16h, o que corresponde a ocupação de 10%.Considerando apenas os leitos de UTI, a taxa de ocupação no estado é de 12%. Maceió registra 19% das UTIs ocupadas. No interior, o percentual é de 4%.", 
             estado_alagoas),

    Noticias(6, 
             "23/06/2021", 
             "A COMISSÃO COVID-19 DA ALAP VISITA PREFEITURA DE AMAPÁ",
             "Deputados saíram satisfeitos com que viram",
             "No início da tarde desta quarta-feira (23) o prefeito Carlos Sampaio (DEM), acompanhado dos secretários: Adervan Mira (secretario de Saúde), Atvaldo Feitosa (secretario adjunto), enfermeira Jesus (Coordenadora de Saúde), coordenadora epidemiológico Walterleny. Recebeu a Comissão da covid-19 da Assembleia legislativa do Estado do Amapá (ALAP), Deputado Estadual Max da AABB (presidente da comissão) e Deputada Estadual Edna Auzier (vice-presidente).Foram tratados assuntos relacionados à vacinação, o prefeito Carlos Sampaio mostrou a comissão que o município tem recebido vacina e cumprido o cronograma de imunização do município. O prefeito explanou quanto à estratégia utilizada no município contra a covid-19. O município foi escolhido pelo Conselho de Secretarias Municipais de Saúde do Amapá (COSEMSAP) a melhor estratégia de combate ao coronavírus regional dae disputa a etapa nacional.A Deputada Edna Auzier recomendará uma moção de aplauso pelo trabalho prestado a luta contra a covid-19 na Assembleia Legislativa (ALAP).Prefeitura de Amapá crescimento e oportunidade.", 
             estado_amapa),

    Noticias(7, 
             "17/03/2021", 
             "UEA monta estrutura para processamento de amostras no estudo CovacManaus",
             "Com o objetivo de agilizar a análise de amostras de sangue extraídas de servidores no estudo CovacManaus, um laboratório de processamento foi montado na Escola Normal Superior da Universidade do Estado do Amazonas (ENS/UEA) especialmente para o projeto.",
             "Com o objetivo de agilizar a análise de amostras de sangue extraídas de servidores no estudo CovacManaus, um laboratório de processamento foi montado na Escola Normal Superior da Universidade do Estado do Amazonas (ENS/UEA) especialmente para o projeto. O local reúne 12 especialistas em Biomedicina e Farmácia responsáveis por armazenar as coletas, que serão enviadas para sorologia no Instituto Butantan, em São Paulo.O laboratório irá concentrar as coletas de sangue de trabalhadores com comorbidades vacinados no projeto e também daqueles que não receberam o imunizante (sem comorbidades), mas que participarão do estudo por meio da sorologia. Ao todo, 10 mil servidores da educação e segurança participarão da pesquisa.A pesquisadora da Fundação de Medicina Tropical Doutor Heitor Vieira Dourado (FMT-HVD), Gisely Melo, explicou que a estrutura existente na universidade foi equipada com aparelhos e insumos. A ideia é dar rapidez no processamento das coletas.", 
             estado_amazonas),
    
    Noticias(8, 
             "27/03/2022", 
             "Guia procura esclarecer relação entre covid-19 e lesões de pele",
             "A Sociedade Brasileira de Dermatologia (SBD) lançou o Guia sobre a Covid-19 e suas manifestações cutâneas",
             "A Sociedade Brasileira de Dermatologia (SBD) lançou o Guia sobre a Covid-19 e suas manifestações cutâneas, destinado a esclarecer a população sobre a relação entre a pandemia e lesões de pele. Ele pode ser acessado no site da SBD. As informações são da Agência Brasil.O coordenador do Departamento de Medicina Interna da SBD, Paulo Criado, disse à Agência Brasil que manifestações que ocorrem na covid-19 não são exclusivas desse vírus. Elas são observadas em outras doenças dermatológicas ou doenças sistêmicas.", 
             estado_bahia),

    Noticias(9, 
             "28/03/2022", 
             "Ceará tem 3º maior percentual de população imunizada contra Covid",
             "Dado é do Consórcio de Veículos de Imprensa. Estado fica atrás apenas de São Paulo, com 89,76% da população imunizada; e Piauí, com 87,70%.",
             "O Ceará é o terceiro estado do país com maior percentual de população com vacinação completa contra a Covid, com 83,07% de pessoas de 5 anos ou mais que receberam as duas doses ou a vacina de dose única. O Estado fica atrás apenas de São Paulo, com 89,76% da população imunizada; e Piauí, com 87,70%. Os dados são do Consórcio de Veículos de Imprensa, a partir das informações repassadas pelas secretarias de saúde de todo o Brasil. O governador Camilo Santana destacou o desempenho da vacinação contra a Covid-19 no Ceará em postagem nas redes sociais. 'Nosso Ceará no topo da vacinação contra a Covid no Brasil. Parabéns aos nossos profissionais de saúde. E viva a ciência', publicou Camilo.", 
             estado_ceara),
    
    Noticias(10, 
             "25/03/2022", 
             "GOVERNO DO ESPÍRITO SANTO DIVULGA 100º MAPA DE RISCO COVID-19",
             "O Governo do Estado anunciou, nesta sexta-feira (25), o 100º Mapa de Risco Covid-19, que terá vigência desta segunda-feira (28) até o próximo domingo (03). ",
             "O Governo do Estado anunciou, nesta sexta-feira (25), o 100º Mapa de Risco Covid-19, que terá vigência desta segunda-feira (28) até o próximo domingo (03). Não houve alterações em relação a classificação da semana anterior. Duas microrregiões já estão classificadas em Risco Muito Baixo, totalizando 12 municípios. Outros 66 municípios estão classificados em Risco Baixo. De acordo com a Portaria da Secretaria da Saúde (Sesa), serão classificadas em Risco Muito Baixo as microrregiões que alcançarem 80% da população adulta com o esquema vacinal primário (segunda dose ou dose única); 90% da população de 12 a 17 anos vacinada com a primeira dose; e 90% da população idosa apta com a dose de reforço. A Matriz de Risco de Convivência considera no eixo de ameaça: o coeficiente de casos ativos por município dos últimos 28 dias, além da quantidade de testes realizados por grupo de mil habitantes e a média móvel de óbitos dos últimos 14 dias. Já o eixo de vulnerabilidade considera a taxa de ocupação de leitos potenciais de UTI exclusivos para tratamento da Covid-19, isto é, a disponibilidade máxima de leitos para tratamento da doença. A estratégia de mapeamento de risco teve início em abril do ano passado.", 
             estado_espirito),
    
    Noticias(11, 
             "28/03/2022", 
             "Atualização sobre a Covid-19 em Goiás e doses da vacina já aplicadas",
             "O Governo de Goiás, por meio da SES-GO, monitora sistematicamente suspeitas de novos casos. Boletim apresenta número de doses da vacina contra o coronavírus já aplicadas em todo o território goiano. ",
             "A Secretaria de Estado da Saúde de Goiás (SES-GO) informa que há 1.272.062 casos de doença pelo coronavírus 2019 (Covid-19) no território goiano. No Estado, há 769.378 casos suspeitos em investigação e 316.923 casos já foram descartados. Há 26.212 óbitos confirmados de Covid-19 em Goiás até o momento, o que significa uma taxa de letalidade de 2,06%. Há 351 óbitos suspeitos que estão em investigação.", 
             estado_goias),

    Noticias(12, 
             "28/03/2022", 
             "Em uma semana, Maranhão registra mais de 2 mil casos de Covid-19",
             "Os registros são de 21 a 28 de março e foram obtidos a partir do boletim epidemiológico divulgado pela Secretaria de Estado da Saúde (SES).",
             "Em uma semana, o Maranhão registrou 2.428 casos e 12 mortes por Covid-19, segundo dados da Secretaria de Estado da Saúde (SES). Os registros são de 21 a 28 de março e foram obtidos a partir do boletim epidemiológico que é divulgado diariamente pela pasta.", 
             estado_maranhao),

    Noticias(13, 
             "04/12/2020", 
             "Mais de 70 mil pessoas foram atendidas no Centro De triagem Covid-19",
             "Em funcionamento há 4 meses, o Centro de Triagem Covid-19 já atendeu 71 mil e 367 pessoas, auxiliando a atenção básica da Baixada Cuiabana no tratamento do coronavírus.",
             "Deste total, 11 mil e 557 testaram positivo para o novo coronavírus, 39 mil e 127 tiveram resultado negativo e 20 mil 683 apresentaram quadro suspeito da doença. Além dos testes para diagnóstico, foram realizadas 5 mil e 293 tomografias, exame de avaliação dos pulmões, que auxilia no quadro clínico e tratamento./ Para os pacientes que testaram positivo, a farmácia da unidade já entregou 32 mil e 240 kits de medicamentos após a consulta médica.", 
             estado_matoGrosso),
             
    Noticias(14, 
             "29/03/2022", 
             "Com 48 internados por Covid, MS segue com hospitalizações em queda",
             "As hospitalizações por Covid continuam em queda no Estado. Boletim epidemiológico divulgado pela Secretaria de Estado de Saúde (SES) nesta terça-feira (29) mostra 48 pessoas internadas em Mato Grosso do Sul.",
             "As hospitalizações por Covid continuam em queda no Estado. Boletim epidemiológico divulgado pela Secretaria de Estado de Saúde (SES) nesta terça-feira (29) mostra 48 pessoas internadas em Mato Grosso do Sul. Neste ano de 2022, o pico de internados foi no dia 10 de fevereiro, com 454 hospitalizados. Desde então, os números vem caindo gradativamente. Mato Grosso do Sul conta atualmente com 2.629 casos ativos, sendo 2.581 em isolamento domiciliar e outros 48 hospitalizados, sendo 21 em leitos clínicos e 27 em leitos de UTI. A taxa global de ocupação de leitos SUS/UTI adulto por macrorregião de internação está em 68% em Campo Grande, 60% em Dourados, 47% em Corumbá e 30% em Três Lagoas. Mato Grosso do Sul registrou 7 óbitos por complicações da Covid, elevando a média móvel que estava em 2,6 para 3,4. Dados do boletim indicam que as mortes ocorreram no período entre 16 de junho de 2021 a 27 de março de 2022, e as vítimas residiam em Campo Grande (3), Dourados (2), Guia Lopes da Laguna (1) e Rochedo (1). ", 
             estado_matoGrossoSul),

    Noticias(15, 
             "14/03/2022", 
             "USO DE MÁSCARAS EM LOCAIS ABERTOS PASSA A SER FACULTATIVO EM MINAS GERAIS",
             "O uso de máscaras de proteção em locais abertos deixa de ser obrigatório em Minas Gerais. A partir do dia 12 de março.",
             "O uso de máscaras de proteção em locais abertos deixa de ser obrigatório em Minas Gerais. A partir do dia 12 de março, a SES-MG recomenda aos municípios mineiros facultarem seu uso de acordo com os indicadores de imunização de seus territórios. A medida é tomada a partir da melhoria dos indicadores da pandemia em Minas Gerais e ao avanço na vacinação. Assim, o critério para a desobrigação em locais abertos é o município ter atingido pelo menos 80% da população com mais de 5 anos com esquema vacinal completo (duas doses ou dose única) da população, e a aplicação da dose de reforço em mais de 40% das pessoas acima de 18 anos.", 
             estado_minas),
        
    Noticias(16, 
             "29/03/2022", 
             "Mais duas mortes por Covid-19 são registradas em Santarém; confira os dados da pandemia",
             "Boletim com dados atualizados foi divulgado pela Secretaria Municipal de Saúde (Semsa) na noite de segunda (28). De acordo com o informe, mortes aconteceram nos dias 22 e 23 de março.",
             "Mais duas mortes por Covid-19 foram registradas em Santarém, no oeste do Pará. Os dados foram atualizados na noite de segunda (28) pela Secretaria Municipal de Saúde (Semsa).De acordo com o informe, as mortes registradas aconteceram nos dias 22 e 23 de março. Uma mulher de 64 anos e um homem de 49, infelizmente, perderam a vida na pandemia. Existem 2 óbitos sendo investigados e 18 pacientes estão em isolamento clínico-hospitalar ou domiciliar. Ainda segundo o informe, há 39.137 casos confirmados no município. Existem 37.815 pessoas recuperadas, 1.306 óbitos, 63.580 resultados negativos, 22 análises, 81 monitorados e 128.377 monitorados já recuperados.", 
             estado_para),
    
    

]