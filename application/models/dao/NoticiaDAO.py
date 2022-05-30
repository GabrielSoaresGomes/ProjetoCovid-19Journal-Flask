from datetime import datetime

from application.models.entities.Noticia import Noticia
from .lista_estados import *

class NoticiaDAO:
        def __init__(self):
                self.lista_noticias = [
                        Noticia(0, 
                                "14/03/2022", 
                                "Mesmo com vazante, três cidades do AC seguem com nível dos rios acima da cota de transbordo",
                                "Estão com nível dos rios acima da cota de transbordo a capital acreana, Rio Branco, Sena Madureira, Porto Acre e Cruzeiro do Sul.",
                                "Alguns rios que estão acima da cota de transbordo apresentaram vazante nesta segunda-feira (28). Entre eles estão o Rio Acre, em Rio Branco, Iaco, em Sena Madureira, e Juruá, em Cruzeiro do Sul, que mesmo assim continuam acima da cota de transbordo, de acordo com o informativo diário da Defesa Civil Estadual.Além destas três cidades, Porto Acre foi o único município onde o Rio Acre apresentou aumento no nível das águas que chegou à cota de 13,22 metros nesta segunda e está a 72 centímetros acima da cota de transbordo, que é de 12,50 metros. Porém, nenhuma família foi removida. Os efeitos da cheia fizeram o governador Gladson Cameli decretar situação de emergência em Feijó, Tarauacá, Sena Madureira, Santa Rosa do Purus, Jordão e Cruzeiro do Sul. O decreto foi publicado no Diário Oficial do Estado (DOE) e tem validade de 90 dias. Feijó e Tarauacá, cidades onde os rio transbordaram na semana passada, os rios Envira (11,70 metros) e Tarauacá (9 metros) voltaram a subir nesta segunda, mas estão abaixo da cota de transbordo, 12 metros e 9,50 metros, respectivamente.", 
                                estado_acre,
                                "https://s2.glbimg.com/LVDbLiR5c2XrSPCbzA9Z3NVAhHM=/0x0:1280x853/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2020/E/t/wLcTMiSAGquliTl3UAqw/covid.jpg"),
                        
                        Noticia(1, 
                                "28/03/2022", 
                                "Alagoas confirma 47 novos casos e mais 4 mortes por Covid",
                                "Estado tem 1.327 casos suspeitos do coronavírus. Total de óbitos chegou a 6.873.",
                                "Alagoas registrou 47 novos casos e mais quatro mortes por Covid nesta segunda-feira (28), de acordo com a Secretaria de Estado da Saúde (Sesau). No último domingo (27), foi a primeira vez desde o início da pandemia, em março de 2020, que o estado não registrou casos e óbitos por Covid.O total acumulado desde o início da pandemia é 296.019 casos conhecidos e 6.873 mortes. Do total de pessoas diagnosticadas com infecção pelo coronavírus, 288.709 estão recuperadas.O estado também acumula 1.327 casos suspeitos, à espera de resultado de exame.Dos 284 leitos exclusivos para Covid e influenza, 29 estavam ocupados até as 16h, o que corresponde a ocupação de 10%.Considerando apenas os leitos de UTI, a taxa de ocupação no estado é de 12%. Maceió registra 19% das UTIs ocupadas. No interior, o percentual é de 4%.", 
                                estado_alagoas,
                                "https://www.saude.al.gov.br/wp-content/uploads/2022/04/Para-se-candidatar-a-doacao-de-sangue-e-necessario-estar-usando-mascara_FOTO_Carla-Cleto-1-300x200.jpg"),

                        Noticia(2, 
                                "23/06/2021", 
                                "A COMISSÃO COVID-19 DA ALAP VISITA PREFEITURA DE AMAPÁ",
                                "Deputados saíram satisfeitos com que viram",
                                "No início da tarde desta quarta-feira (23) o prefeito Carlos Sampaio (DEM), acompanhado dos secretários: Adervan Mira (secretario de Saúde), Atvaldo Feitosa (secretario adjunto), enfermeira Jesus (Coordenadora de Saúde), coordenadora epidemiológico Walterleny. Recebeu a Comissão da covid-19 da Assembleia legislativa do Estado do Amapá (ALAP), Deputado Estadual Max da AABB (presidente da comissão) e Deputada Estadual Edna Auzier (vice-presidente).Foram tratados assuntos relacionados à vacinação, o prefeito Carlos Sampaio mostrou a comissão que o município tem recebido vacina e cumprido o cronograma de imunização do município. O prefeito explanou quanto à estratégia utilizada no município contra a covid-19. O município foi escolhido pelo Conselho de Secretarias Municipais de Saúde do Amapá (COSEMSAP) a melhor estratégia de combate ao coronavírus regional dae disputa a etapa nacional.A Deputada Edna Auzier recomendará uma moção de aplauso pelo trabalho prestado a luta contra a covid-19 na Assembleia Legislativa (ALAP).Prefeitura de Amapá crescimento e oportunidade.", 
                                estado_amapa,
                                "data:image/jpeg;base64,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"),

                        Noticia(3,
                                "17/03/2021", 
                                "UEA monta estrutura para processamento de amostras no estudo CovacManaus",
                                "Com o objetivo de agilizar a análise de amostras de sangue extraídas de servidores no estudo CovacManaus, um laboratório de processamento foi montado na Escola Normal Superior da Universidade do Estado do Amazonas (ENS/UEA) especialmente para o projeto.",
                                "Com o objetivo de agilizar a análise de amostras de sangue extraídas de servidores no estudo CovacManaus, um laboratório de processamento foi montado na Escola Normal Superior da Universidade do Estado do Amazonas (ENS/UEA) especialmente para o projeto. O local reúne 12 especialistas em Biomedicina e Farmácia responsáveis por armazenar as coletas, que serão enviadas para sorologia no Instituto Butantan, em São Paulo.O laboratório irá concentrar as coletas de sangue de trabalhadores com comorbidades vacinados no projeto e também daqueles que não receberam o imunizante (sem comorbidades), mas que participarão do estudo por meio da sorologia. Ao todo, 10 mil servidores da educação e segurança participarão da pesquisa.A pesquisadora da Fundação de Medicina Tropical Doutor Heitor Vieira Dourado (FMT-HVD), Gisely Melo, explicou que a estrutura existente na universidade foi equipada com aparelhos e insumos. A ideia é dar rapidez no processamento das coletas.", 
                                estado_amazonas,
                                "https://s2.glbimg.com/IIY1B7JqzQd8VE_X5Heok3l3aFg=/0x0:1024x683/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2020/M/Z/fdgBblRA2y4bEYzp2d5w/hospital.jpg"),


                        Noticia(4, 
                                "27/03/2022", 
                                "Guia procura esclarecer relação entre covid-19 e lesões de pele",
                                "A Sociedade Brasileira de Dermatologia (SBD) lançou o Guia sobre a Covid-19 e suas manifestações cutâneas",
                                "A Sociedade Brasileira de Dermatologia (SBD) lançou o Guia sobre a Covid-19 e suas manifestações cutâneas, destinado a esclarecer a população sobre a relação entre a pandemia e lesões de pele. Ele pode ser acessado no site da SBD. As informações são da Agência Brasil.O coordenador do Departamento de Medicina Interna da SBD, Paulo Criado, disse à Agência Brasil que manifestações que ocorrem na covid-19 não são exclusivas desse vírus. Elas são observadas em outras doenças dermatológicas ou doenças sistêmicas.", 
                                estado_bahia,
                                "https://sosvida.com.br/wp-content/uploads/2021/10/reducao-casos-covid.jpg"),

                        Noticia(5, 
                                "28/03/2022", 
                                "Ceará tem 3º maior percentual de população imunizada contra Covid",
                                "Dado é do Consórcio de Veículos de Imprensa. Estado fica atrás apenas de São Paulo, com 89,76% da população imunizada; e Piauí, com 87,70%.",
                                "O Ceará é o terceiro estado do país com maior percentual de população com vacinação completa contra a Covid, com 83,07% de pessoas de 5 anos ou mais que receberam as duas doses ou a vacina de dose única. O Estado fica atrás apenas de São Paulo, com 89,76% da população imunizada; e Piauí, com 87,70%. Os dados são do Consórcio de Veículos de Imprensa, a partir das informações repassadas pelas secretarias de saúde de todo o Brasil. O governador Camilo Santana destacou o desempenho da vacinação contra a Covid-19 no Ceará em postagem nas redes sociais. 'Nosso Ceará no topo da vacinação contra a Covid no Brasil. Parabéns aos nossos profissionais de saúde. E viva a ciência', publicou Camilo.", 
                                estado_ceara,
                                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGzZawsX2Pnq2qKKrgCEfQHcsjDVlJmxVkvBBPbWMTL-78T7qdguuL1i-1pzHH1hvSZQ4&usqp=CAU"),
                        
                        Noticia(6, 
                                "25/03/2022", 
                                "GOVERNO DO ESPÍRITO SANTO DIVULGA 100º MAPA DE RISCO COVID-19",
                                "O Governo do Estado anunciou, nesta sexta-feira (25), o 100º Mapa de Risco Covid-19, que terá vigência desta segunda-feira (28) até o próximo domingo (03). ",
                                "O Governo do Estado anunciou, nesta sexta-feira (25), o 100º Mapa de Risco Covid-19, que terá vigência desta segunda-feira (28) até o próximo domingo (03). Não houve alterações em relação a classificação da semana anterior. Duas microrregiões já estão classificadas em Risco Muito Baixo, totalizando 12 municípios. Outros 66 municípios estão classificados em Risco Baixo. De acordo com a Portaria da Secretaria da Saúde (Sesa), serão classificadas em Risco Muito Baixo as microrregiões que alcançarem 80% da população adulta com o esquema vacinal primário (segunda dose ou dose única); 90% da população de 12 a 17 anos vacinada com a primeira dose; e 90% da população idosa apta com a dose de reforço. A Matriz de Risco de Convivência considera no eixo de ameaça: o coeficiente de casos ativos por município dos últimos 28 dias, além da quantidade de testes realizados por grupo de mil habitantes e a média móvel de óbitos dos últimos 14 dias. Já o eixo de vulnerabilidade considera a taxa de ocupação de leitos potenciais de UTI exclusivos para tratamento da Covid-19, isto é, a disponibilidade máxima de leitos para tratamento da doença. A estratégia de mapeamento de risco teve início em abril do ano passado.", 
                                estado_espirito,
                                'https://alegre.ufes.br/sites/alegre.ufes.br/files/styles/imagem_conteudo/public/field/image/yellow_modern_creative_corporate_social_media_strategy_presentation.png?itok=0nsNlEO-'),
                        
                        Noticia(7, 
                                "28/03/2022", 
                                "Atualização sobre a Covid-19 em Goiás e doses da vacina já aplicadas",
                                "O Governo de Goiás, por meio da SES-GO, monitora sistematicamente suspeitas de novos casos. Boletim apresenta número de doses da vacina contra o coronavírus já aplicadas em todo o território goiano. ",
                                "A Secretaria de Estado da Saúde de Goiás (SES-GO) informa que há 1.272.062 casos de doença pelo coronavírus 2019 (Covid-19) no território goiano. No Estado, há 769.378 casos suspeitos em investigação e 316.923 casos já foram descartados. Há 26.212 óbitos confirmados de Covid-19 em Goiás até o momento, o que significa uma taxa de letalidade de 2,06%. Há 351 óbitos suspeitos que estão em investigação.", 
                                estado_goias,
                                'https://cosemsgo.org.br/wp-content/uploads/2021/01/Plano-Estadual-Vacinacao.jpg'),

                        Noticia(8, 
                                "28/03/2022", 
                                "Em uma semana, Maranhão registra mais de 2 mil casos de Covid-19",
                                "Os registros são de 21 a 28 de março e foram obtidos a partir do boletim epidemiológico divulgado pela Secretaria de Estado da Saúde (SES).",
                                "Em uma semana, o Maranhão registrou 2.428 casos e 12 mortes por Covid-19, segundo dados da Secretaria de Estado da Saúde (SES). Os registros são de 21 a 28 de março e foram obtidos a partir do boletim epidemiológico que é divulgado diariamente pela pasta.", 
                                estado_maranhao,
                                'https://www.corona.ma.gov.br/public/assets/img/share2.jpg?=20220402'),

                        Noticia(9, 
                                "04/12/2020", 
                                "Mais de 70 mil pessoas foram atendidas no Centro De triagem Covid-19",
                                "Em funcionamento há 4 meses, o Centro de Triagem Covid-19 já atendeu 71 mil e 367 pessoas, auxiliando a atenção básica da Baixada Cuiabana no tratamento do coronavírus.",
                                "Deste total, 11 mil e 557 testaram positivo para o novo coronavírus, 39 mil e 127 tiveram resultado negativo e 20 mil 683 apresentaram quadro suspeito da doença. Além dos testes para diagnóstico, foram realizadas 5 mil e 293 tomografias, exame de avaliação dos pulmões, que auxilia no quadro clínico e tratamento./ Para os pacientes que testaram positivo, a farmácia da unidade já entregou 32 mil e 240 kits de medicamentos após a consulta médica.", 
                                estado_matoGrosso,
                                'https://i0.wp.com/www.conass.org.br/wp-content/uploads/2021/12/131221093011.jpeg?fit=448%2C299&ssl=1'),
                                
                        Noticia(11, 
                                "29/03/2022", 
                                "Com 48 internados por Covid, MS segue com hospitalizações em queda",
                                "As hospitalizações por Covid continuam em queda no Estado. Boletim epidemiológico divulgado pela Secretaria de Estado de Saúde (SES) nesta terça-feira (29) mostra 48 pessoas internadas em Mato Grosso do Sul.",
                                "As hospitalizações por Covid continuam em queda no Estado. Boletim epidemiológico divulgado pela Secretaria de Estado de Saúde (SES) nesta terça-feira (29) mostra 48 pessoas internadas em Mato Grosso do Sul. Neste ano de 2022, o pico de internados foi no dia 10 de fevereiro, com 454 hospitalizados. Desde então, os números vem caindo gradativamente. Mato Grosso do Sul conta atualmente com 2.629 casos ativos, sendo 2.581 em isolamento domiciliar e outros 48 hospitalizados, sendo 21 em leitos clínicos e 27 em leitos de UTI. A taxa global de ocupação de leitos SUS/UTI adulto por macrorregião de internação está em 68% em Campo Grande, 60% em Dourados, 47% em Corumbá e 30% em Três Lagoas. Mato Grosso do Sul registrou 7 óbitos por complicações da Covid, elevando a média móvel que estava em 2,6 para 3,4. Dados do boletim indicam que as mortes ocorreram no período entre 16 de junho de 2021 a 27 de março de 2022, e as vítimas residiam em Campo Grande (3), Dourados (2), Guia Lopes da Laguna (1) e Rochedo (1). ", 
                                estado_matoGrossoSul,
                                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5fCnAub0fmEg5Pm44DYzmyXMMjKag9tcBBg&usqp=CAU'),

                        Noticia(12, 
                                "14/03/2022", 
                                "USO DE MÁSCARAS EM LOCAIS ABERTOS PASSA A SER FACULTATIVO EM MINAS GERAIS",
                                "O uso de máscaras de proteção em locais abertos deixa de ser obrigatório em Minas Gerais. A partir do dia 12 de março.",
                                "O uso de máscaras de proteção em locais abertos deixa de ser obrigatório em Minas Gerais. A partir do dia 12 de março, a SES-MG recomenda aos municípios mineiros facultarem seu uso de acordo com os indicadores de imunização de seus territórios. A medida é tomada a partir da melhoria dos indicadores da pandemia em Minas Gerais e ao avanço na vacinação. Assim, o critério para a desobrigação em locais abertos é o município ter atingido pelo menos 80% da população com mais de 5 anos com esquema vacinal completo (duas doses ou dose única) da população, e a aplicação da dose de reforço em mais de 40% das pessoas acima de 18 anos.", 
                                estado_minas,
                                'https://s2.glbimg.com/yqALgsR7JZuq_ehOxqB09eWBTzI=/0x0:2048x1366/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2022/A/q/CDfNkFTl2c5ShQGaj2pA/20210323145938-ap2a9408.jpg'),
                                
                        Noticia(13, 
                                "29/03/2022", 
                                "Mais duas mortes por Covid-19 são registradas em Santarém; confira os dados da pandemia",
                                "Boletim com dados atualizados foi divulgado pela Secretaria Municipal de Saúde (Semsa) na noite de segunda (28). De acordo com o informe, mortes aconteceram nos dias 22 e 23 de março.",
                                "Mais duas mortes por Covid-19 foram registradas em Santarém, no oeste do Pará. Os dados foram atualizados na noite de segunda (28) pela Secretaria Municipal de Saúde (Semsa).De acordo com o informe, as mortes registradas aconteceram nos dias 22 e 23 de março. Uma mulher de 64 anos e um homem de 49, infelizmente, perderam a vida na pandemia. Existem 2 óbitos sendo investigados e 18 pacientes estão em isolamento clínico-hospitalar ou domiciliar. Ainda segundo o informe, há 39.137 casos confirmados no município. Existem 37.815 pessoas recuperadas, 1.306 óbitos, 63.580 resultados negativos, 22 análises, 81 monitorados e 128.377 monitorados já recuperados.", 
                                estado_para,
                                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSW-Emspm-scZn3bIweaj-z4AjRW_nOcKOfdg&usqp=CAU'),

                        Noticia(14,
                                "30/03/2022",
                                "Atualização Covid-19",
                                "Paraíba registra 585 novos casos de covid-19 nesta quarta",
                                "A Secretaria de Estado da Saúde (SES) registrou, nesta quarta (30), 585 casos de Covid-19. Entre os casos confirmados neste boletim, 02 (0,34%) são moderados ou graves e 583 (99,66%) são leves. Agora, a Paraíba totaliza 595.932 casos confirmados da doença, que estão distribuídos por todos os 223 municípios. Até o momento, já foram realizados 1.493.728 testes para diagnóstico da Covid-19.",
                                estado_paraiba,
                                'https://tce.pb.gov.br/noticias/tce-pb-analisa-acoes-e-gastos-do-estado-e-municipios-para-combate-a-covid-19-e-faz-recomendacoes-aos-gestores/covid-19.jpg'),

                        Noticia(15,
                                "30/03/2022",
                                "Coronavírus no Paraná: Acompanhe as notícias do estado em relação à pandemia",
                                "O estado do Paraná divulgou nesta quarta-feira (30), 2.203 novos casos de Covid-19 e 18 mortes provocadas pelo coronavírus. 2.173.502 pacientes se recuperaram.",
                                "De acordo com a Secretaria Estadual de Saúde, 9.788.661 milhões de paranaenses receberam, ao menos, uma dose da vacina; 9.064.090 milhões receberam duas doses ou imunizante de dose única. O estado do Paraná divulgou, nesta terça-feira (29), 2.303 novos casos de Covid-19 e 16 mortes provocadas pelo coronavírus. 2.159.992 pacientes se recuperaram.",
                                estado_parana,
                                'https://www.saude.pr.gov.br/sites/default/arquivos_restritos/files/imagem/2020-06/informes_banner_covid_19.png'),

                        Noticia(16,
                                "30/03/2022",
                                "Coronavírus no Pernambuco Acompanhe as notícias do estado em relação à pandemia",
                                "Vacinação itinerante acontece em seis locais da capital. Há locais fixos para a testagem gratuita da população na cidade, a maioria deles com necessidade de marcação prévia.",
                                "A vacinação itinerante contra a Covid-19 para pessoas a partir de 12 anos acontece em seis locais do Recife nesta quarta-feira (30). Também há imunização mediante agendamento para todos a partir de 5 anos, incluindo a aplicação da 4ª dose para pessoas a partir de 65 anos. Além disso, há locais para a testagem gratuita na capital, a maioria através de marcação prévia (confira locais mais abaixo). Nesta última semana de março, a programação da vacinação itinerante na capital pernambucana segue até sexta-feira (1º). O atendimento acontece sem necessidade de marcação e, para receber a dose, os moradores precisam ter um documento de identificação com foto e um comprovante de residência.",
                                estado_pernambuco,
                                'https://www.salgueiro.pe.gov.br/covid19/imagens/salgueiro-covid-19-qd.png'),

                        Noticia(17,
                                "31/03/2022",
                                "Piauí volta a não registrar mortes por Covid nas últimas 24 horas; terceira vez esta semana",
                                "O estado registrou 31 casos confirmados, segundo o boletim da Secretaria de Estado da Saúde, nesta quinta-feira (31).",
                                "O Piauí registrou 31 casos confirmados e nenhum óbito por Covid-19, nas últimas 24 horas, segundo dados divulgados pela Secretaria de Estado da Saúde, nesta quinta-feira (31). Dos 31 casos confirmados 21 são de mulheres e 10 de homens, com idades que variam de 02 a 78 anos. Os casos confirmados no estado somam 367.701 em todos os municípios piauienses. Já os óbitos pelo novo coronavírus chegam 7.728 casos e foram registrados em 224 municípios. Dos leitos existentes na rede de saúde do Piauí para atendimento à Covid-19, 102 estão ocupados, sendo 66 leitos clínicos, 29 UTI’s e 07 leitos de estabilização. As altas acumuladas somam 25.995 até o dia 31 de março de 2022.",
                                estado_piaui,
                                'http://cosemspi.org.br/wp-content/uploads/2022/01/Covid-19-Site.png'),

                        Noticia(18,
                                "01/04/2022",
                                "Vacinação contra a gripe no Rio começa na segunda-feira",
                                "Imunização será em etapa e, segundo a Secretaria Municipal de Saúde, só crianças com comorbidades precisam fazer um intervalo entre dose da vacina contra a Covid e a da gripe.",
                                "Começa na próxima segunda-feira (4) a vacinação contra a gripe no Rio. O processo de imunização será em etapas, iniciando pelos grupos prioritários.A Secretaria Municipal de Saúde informou que só crianças de 5 a 11 anos precisam esperar um intervalo de tempo para serem vacinadas com nova dose da vacina contra a Covid e a contra a gripe. O intervalo indicado é de 15 dias entre a aplicação dos imunizantes. A orientação da secretaria é que quem estiver com sintomas sugestivos de Covid deve adiar a vacinação contra a gripe até ficar totalmente recuperado. Além disso, precisa esperar pelo menos quatro semanas após o início dos sintomas.",
                                estado_rioDeJaneiro,
                                'https://conteudo.imguol.com.br/c/noticias/0a/2020/04/13/13abr2020---com-foco-de-covid-19-duque-de-caxias-rj-tem-fila-de-8-horas-em-upa-e-comercio-aberto-1586810529826_v2_4x3.jpg'),

                        Noticia(19,
                                "01/04/2022",
                                "Governo do RN prorroga obrigatoriedade do uso de máscaras em locais fechados até 7 de abril",
                                "Decreto foi publicado no Diário Oficial do Estado desta sexta-feira (1º).",
                                "O governo do Rio Grande do Norte prorrogou a obrigatoriedade do uso de máscaras em locais fechados até 7 de abril, segundo o boletim da Secretaria de Saúde, nesta quarta-feira.",
                                estado_rioGrandeNorte,
                                'https://portalcovid19.saude.rn.gov.br/wp-content/uploads/2020/06/IMG000000000233260.jpg'),

                        Noticia(20,
                                "01/04/2022",
                                "Março encerra com 777 mortes por Covid no RS, queda de 44% em relação ao mês anterior",
                                "Secretaria Estadual da Saúde confirmou mais 13 óbitos nesta quinta (31). Internados em leitos de UTI com confirmação ou suspeita para coronavírus baixa para 11%.",
                                "Março encerra, nesta quinta-feira (31), com mais 13 mortes por Covid-19 no Rio Grande do Sul. Com elas, foram 777 óbitos no mês, uma queda de 44,4% em relação a fevereiro, o mais letal nos últimos oito meses. A redução confirma a tendência de atenuamento na pandemia. Agora, o estado retorna a patamares semelhantes a agosto do ano passado, ainda que superior aos cinco meses posteriores.Em toda a pandemia, o Rio Grande do Sul tem 39.049 vítimas. As mais recentes foram identificadas pela Secretaria Estadual da Saúde (SES) entre 5 e 30 de março, exceto uma de fevereiro e outras três de janeiro.",
                                estado_rioGrandeSul,
                                'https://amanha.com.br/images/p/13985/Novos-leitos-de-UTI-Covid-no-HPS-em-Porto-Alegre.jpg'),

                        Noticia(21,
                                "31/03/2022",
                                "ALE-RO derruba veto do governo e médicos da Bolívia poderão atuar em cidades Rondônia sem o Revalida",
                                "Na justificativa, o autor do projeto defende que a fronteira rondoniense está 'desassistida de serviços básicos de saúde'. O Projeto de Lei foi vetado pelo governo por possuir inconstitucionalidade formal.",
                                "Os deputados estaduais derrubaram com unanimidade, na quarta-feira (30), o veto do Governo de Rondônia no Projeto de Lei que autoriza o poder público a contratar médicos estrangeiros, sem o Revalida, para atuar nas cidades do estado que fazem fronteira com a Bolívia. Na justificativa, o autor do projeto, deputado Lebrão, defende que a fronteira rondoniense está 'desassistida de serviços básicos de saúde' e os brasileiros que vivem lá não podem exercer suas funções. O Projeto de Lei foi vetado pelo governo por possuir inconstitucionalidade formal.",
                                estado_rondonia,
                                'https://tcero.tc.br/wp-content/uploads/2021/11/reuniao-saude-2-390x220.jpg'),
                        Noticia(22,
                                "31/03/2022",
                                "SC anuncia fim do estado de calamidade pública por causa da Covid; saiba o que muda",
                                "Decreto acaba nesta quinta-feira (31) e não será renovado. Com a decisão, o Centro de Operações em Emergências em Saúde (COES) deixa de existir.",
                                "O governador de Santa Catarina, Carlos Moisés (Republicanos), confirmou nesta quinta-feira (31) que não irá prorrogar o estado de calamidade pública por conta da pandemia de Covid-19 no estado. O decreto tem validade até as 23h59 de hoje. Com a nova decisão, o Centro de Operações em Emergências em Saúde (COES) deixa de existir. Criado no início da pandemia, o órgão foi responsável para dar suporte nas decisões tomadas pelos prefeitos e secretários no enfrentamento contra o avanço da doença. A Secretaria de Estado da Saúde informou, porém, que o mapa de risco da Covid divulgado semanalmente e os boletins diários, com os números de casos, mortes e ocupação de leitos de Unidade de Terapia Intensiva (UTI), vão continuar.",
                                estado_santaCatarina,
                                'https://www.majorvieira.sc.gov.br/uploads/729/imagens/2918752.jpeg'),
                        
                        Noticia(23,
                                "30/03/2022",
                                "Número de internações por COVID-19 caiu 84% desde janeiro em SP",
                                "Estado está há oito semanas seguidas com queda nas novas internações",
                                "O Governador João Doria anunciou nesta quarta-feira (30) que o Estado de São Paulo registrou redução de 84% das internações por COVID-19 desde o final de janeiro, quando foi registrado o pico da variante Ômicron. Atualmente os hospitais possuem 1.869 pacientes internados, sendo 1.195 em enfermaria e 672 em UTI (Unidade de Terapia Intensiva). 'É uma notícia para ser celebrada. As internações vêm caindo há oito semanas e hoje, pelo quinto dia seguido, São Paulo tem menos de 2 mil pessoas internadas em UTI e em enfermaria'.",
                                estado_saoPaulo,
                                'https://www.cnnbrasil.com.br/wp-content/uploads/sites/12/2021/10/ubs_posto_vacinacao_covid_19_sao_paulo_sp.jpg?w=1200&h=900&crop=1'),
                        
                        Noticia(24,
                                '01/04/2022',
                                "Sergipe inicia campanha de vacinação contra a Influenza na próxima segunda, 04 de abril",
                                "Sergipe inicia a 24ª campanha nacional de vacinação contra a gripe Influenza a partir da próxima segunda, dia 04 de abril.",
                                "Sergipe inicia a 24ª campanha nacional de vacinação contra a gripe Influenza a partir da próxima segunda, dia 04 de abril. O calendário de aplicação dos imunizantes foi definido pela Secretaria de Estado da Saúde (SES) em duas etapas que foram delimitadas pelo Ministério da Saúde e contemplam diversos grupos prioritários. A vacina que será aplicada é trivalente, ou seja, protege contra os vírus H1N1, H3N2 e a influenza A.'Daremos início à campanha vacinando dois grupos prioritários: trabalhadores da Saúde, que também terão a vacina do sarampo atualizada e idosos com faixa etária de 60 anos e mais. Além disso, a SES vai promover em 30 de abril, o dia ‘D’ de imunização para reforçar a vacinação desses dois grupos prioritários' ”, explica a Gerente Estadual do Programa de Imunização, Sândala Oliveira.",
                                estado_sergipe,
                                'https://s2.glbimg.com/bZ0fx9o7qkRSQEVMVQbq1dbbprI=/0x0:600x398/984x0/smart/filters:strip_icc()/s.glbimg.com/jo/g1/f/original/2013/04/26/7bde1b0188c63d92c9241dca8b929ee0.jpg'),

                        Noticia(25,
                                '01/04/2022',
                                'Acompanhe o 702º boletim epidemiológico da Covid-19 no Tocantins 01/04',
                                "Hoje o Tocantins contabilizou 184 novos casos confirmados da Covid-19, sendo 22 nas últimas 24h.",
                                "Hoje o Tocantins contabilizou 184 novos casos confirmados da Covid-19, sendo 22 nas últimas 24h. O restante são de exames coletados em dias anteriores e que tiveram seus resultados inseridos no sistema, pelos municípios, na data de ontem. Dos 184 novos casos, 128 foram detectados por RT-PCR, 2 por sorologia e 54 por testes rápidos. Atualmente, o Tocantins contabiliza 922.090 pessoas notificadas com a Covid-19 e acumula 303.003 casos confirmados. Destes 296.799 estão recuperados, 2.059 pacientes seguem em isolamento domiciliar ou hospitalar 4.145 foram a óbito. Os dados contidos no boletim são consolidados com resultados de exames realizados no Lacen e notificações recebidas dos municípios até as 23h59 do último dia.",
                                estado_tocantins,
                                'https://conexaoto.nyc3.digitaloceanspaces.com/image/126093_768x450_width.jpg'),
                        Noticia(26,
                                '01/04/2022',
                                "Covid-19: Distrito Federal começa a aplicar quarta dose em idosos",
                                "Receberá a vacina, a partir de hoje, quem tem mais de 80 anos",
                                "O governo do Distrito Federal (GDF) começa hoje (1º) a aplicar a quarta dose da vacina contra a covid-19 em idosos com mais de 80 anos. De acordo com estimativa da Companhia de Planejamento do Distrito Federal (Codeplan), residem no DF cerca de 40 mil idosos com mais de 80 anos. O GDF recebeu 47.970 doses da Pfizer para imunizar essa população. A Secretaria de Saúde informou que já foram aplicadas 6 milhões de doses de vacina contra a covid-19. Isso equivale a 89,73% da população com a primeira dose; 82,23% com a segunda; 38,70% com a dose de reforço. A Secretaria de Saúde informou que já foram aplicadas 6 milhões de doses de vacina contra a covid-19. Isso equivale a 89,73% da população com a primeira dose; 82,23% com a segunda; 38,70% com a dose de reforço.",
                                estado_distritoFederal,
                                'https://vtb.r7.com/399594/2022/03/29/62438ef543527f1b81000670/cce0aac1015f42bf966b22b17892473d__ER7_DR_TERRASPUBLICAS2903_thumb_thumb.jpg'),
                        ]
                        
        def get_noticia_lista(self):
                return self.lista_noticias

        def set_noticia_lista(self, noticia_lista):
                self.lista_noticias = noticia_lista

        def buscar_noticia(self, id_noticia):
                for noticia in self.lista_noticias:
                        if int(noticia.get_id()) == int(id_noticia):
                                noticia.views += 1
                                return noticia
                return False
        
        def get_mais_curtidas(self):
                mais_curtidas = []
                for noticia in self.get_noticia_lista:
                        if len(mais_curtidas) <= 4:
                                mais_curtidas.append(noticia)
                        elif noticia.likes > mais_curtidas[0].likes:
                                mais_curtidas.insert(0, noticia)
                        elif noticia.likes > mais_curtidas[1].likes:
                                mais_curtidas.insert(1, noticia)
                        elif noticia.likes > mais_curtidas[2].likes:
                                mais_curtidas.insert(2, noticia)
                        elif noticia.likes > mais_curtidas[3].likes:
                                mais_curtidas.insert(3, noticia)
                        elif noticia.likes > mais_curtidas[4].likes:
                                mais_curtidas.insert(4, noticia)
                nova_mais_curtidas = []
                for c in range(0,4):
                        nova_mais_curtidas.append(mais_curtidas[c])
                return nova_mais_curtidas
        
        def get_mais_vistas(self):
                mais_vistas = []
                for noticia in self.get_noticia_lista:
                        if len(mais_vistas) <= 4:
                                mais_vistas.append(noticia)
                        elif noticia.views > mais_vistas[0].views:
                                mais_vistas.insert(0, noticia)
                        elif noticia.views > mais_vistas[1].views:
                                mais_vistas.insert(1, noticia)
                        elif noticia.views > mais_vistas[2].views:
                                mais_vistas.insert(2, noticia)
                        elif noticia.views > mais_vistas[3].views:
                                mais_vistas.insert(3, noticia)
                        elif noticia.views > mais_vistas[4].views:
                                mais_vistas.insert(4, noticia)
                nova_mais_vistas = []
                for c in range(0,4):
                        nova_mais_vistas.append(mais_vistas[c])
                return nova_mais_vistas

        def get_mais_recentes(self):
                mais_recentes = []
                for noticia in self.get_noticia_lista:
                        data = datetime.strptime(noticia.get_dataPostagem(), "%d/%m/%Y")
                        if len(mais_recentes) <= 4:
                                mais_recentes.append(noticia)
                        elif data > datetime.strptime(mais_recentes[0].get_dataPostagem(), "%d/%m/%Y"):
                                mais_recentes.insert(0, noticia)
                        elif data > datetime.strptime(mais_recentes[1].get_dataPostagem(), "%d/%m/%Y"):
                                mais_recentes.insert(1, noticia)
                        elif data > datetime.strptime(mais_recentes[2].get_dataPostagem(), "%d/%m/%Y"):
                                mais_recentes.insert(2, noticia)
                        elif data > datetime.strptime(mais_recentes[3].get_dataPostagem(), "%d/%m/%Y"):
                                mais_recentes.insert(3, noticia)
                        elif data > datetime.strptime( mais_recentes[4].get_dataPostagem(), "%d/%m/%Y"):
                                mais_recentes.insert(4, noticia)
                nova_mais_recentes = []
                for c in range(0,4):
                        nova_mais_recentes.append(mais_recentes[c])
                return nova_mais_recentes


