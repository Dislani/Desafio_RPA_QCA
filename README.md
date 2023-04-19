# Desafio_RPA_QCA
Desafio de automação proposto no processo seletivo da Queiroz Cavalcanti Advocacia (QCA). 

O desafio consiste em criar um *RPA* que realize uma cadeia de ações simuladas, que irão resultar em um download de arquivo presente num site, e posteriormente enviá-lo através de um e-mail.

O desafio tem duas fases, uma que consistem na automatização do acesso a página principal, onde realizaremos o download de um arquivo chamado *bairro.csv*. E a outra fase que consite na automatização do envio do arquivo *bairro.csv* através de um e-mail.

## 1º Parte - Download Automatizado do Arquivo bairro.csv

Foi disponibilizado a *URL* da página principal a ser acessada pelo robô, para que ele siga o fluxo simulando ações de um usuário comum, clicando

Para que fosse possível seguir o fluxo de ações de um usuário simulado, foi disponibilizado inicialmente a *URL* contendo o endereço da página principal a ser acessada pelo robô.

Simulando um usuário, o robô segue o seguinte fluxo de ações:

1. Inicializa o navegador Chrome através do *WebDriver*, e acessa a página principal (*http://dados.recife.pe.gov.br/organization*);
2. Na página principal, clica em Secretaria de *Infraestrutura e Serviços Urbanos*;
3. Após acessar a página do item 2, o robô deverá clicar em *Área Urbana*;
4. Em *Área Urbana*, o robô deverá clicar em *Bairros do Recife*;
5. E por fim, na página dos *Bairros do Recife*, o robô clica no botão **Explorar** e em seguida clica em **Baixar**.

Seguindo estas ações, o robô faz de forma automática o download de um arquivo chamado *bairro.csv*.

## 2º Parte - Envio de E-mail Contendo em Anexo o Arquivo bairro.csv

Nesta segunda fase, o robô estabelece uma conexão com o servidor *SMTP* do *Office365*, para que possamos enviar um e-mail tendo como anexo o arquivo *bairro.csv*.

Para isso, o robô segue as seguintes ações:

1. Estabelece conexão com servidor *SMTP* do *Office365*;
2. Realiza login com uma conta de e-mail configurada no código;
3. Anexa o arquivo *bairro.csv* ao e-mail;
4. Envia o e-mail para o destinatário configurado no código.
