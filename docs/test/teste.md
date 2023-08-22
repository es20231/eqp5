# Teste da Aplicação

## Testes Unitários (CT-TU)

### CT-TU-01 Teste de Unidade para o Componente SignIn.vue:

* CT-TU-01-C1: verificar se o componente foi renderizado;
* CT-TU-01-C2: verificar se o botão foi renderizado;
* CT-TU-01-C3: verificar se os valores de entrada são atualizados ao inserir;
* CT-TU-01-C4: verificar se é disparado um erro ao se inserir um e-mail inválido;
* CT-TU-01-C5: verificar se é disparado um erro ao se inserir uma senha inválida;
* CT-TU-01-C6: verificar se é disparado um pop-up avisando de um erro 401.

### CT-TU-02 Teste de Unidade para o Componente SignUp.vue:

* CT-TU-02-C1: verificar se o componente foi renderizado;
* CT-TU-02-C2: verificar se o botão foi renderizado;
* CT-TU-02-C3: verificar se o valores de entrada são atualizados ao inserir;
* CT-TU-02-C4: verificar se é disparado um erro ao se inserir um username inválido;
* CT-TU-02-C5: verificar se é disparado um erro ao se inserir um nome completo inválido;
* CT-TU-02-C6: verificar se é disparado um erro ao se inserir um e-mail inválido;
* CT-TU-02-C7: verificar se é disparado um erro ao se inserir um senha inválida;
* CT-TU-02-C8: verificar se é disparado um erro ao se inserir uma confirmação de senha
               diferente da original;
* CT-TU-02-C9: verificar se é disparado um erro de resposta ao tentar se cadastrar.

### CT-TU-03 Teste de Unidade para o Componente ForgotPassword.vue:

* CT-TU-03-C1: verificar se o componente foi renderizado;
* CT-TU-03-C2: verificar se o botão foi renderizado;
* CT-TU-03-C3: verificar se o e-mail está conforme o inserido;
* CT-TU-03-C4: verificar se é disparado um erro ao se inserir um e-mail inválido;
* CT-TU-03-C5: verificar se é disparado uma mensagem de erro 401.

### CT-TU-04 Teste de Unidade para o Componente ModalError.vue:

* CT-TU-04-C1: verificar se o componente foi renderizado;
* CT-TU-04-C2: verificar se a mensagem de erro é inserida em sua variável;
* CT-TU-04-C3: verificar se a mensagem de erro é exibida na tela;
* CT-TU-04-C4: verificar se a mensagem de erro é fechada normalmente.

### CT-TU-05 Teste de Unidade para o Componente Layout.vue:

* CT-TU-05-C1: verificar se o componente foi renderizado;
* CT-TU-05-C2: verificar se é possível transitar entre as páginas normalmente;
* CT-TU-05-C3: verificar se o sidebar e o navbar foram renderizados;
* CT-TU-05-C4: verificar se a tela reage ao encolhimento com o método isSmallScreen().

### CT-TU-06 Teste de Unidade para o Componente Navbar.vue:

* CT-TU-06-C1: verificar se o componente foi renderizado;
* CT-TU-06-C2: verificar se os links foram renderizado;
* CT-TU-06-C3: verificar se é disparado um erro quando os dados são perdidos em meio a
               conexão;
* CT-TU-06-C4: verificar se é possível transitar entre as páginas normalmente.

### CT-TU-07 Teste de Unidade para o Componente Sidebar.vue:

* CT-TU-07-C1: verificar se o componente foi renderizado;
* CT-TU-07-C2: verificar se a imagem de perfil está renderizando;
* CT-TU-07-C3: verificar se é disparado um erro de conexão ao tentar fazer logout;
* CT-TU-07-C4: verificar se o link para a página 'gallery' está funcionando.

### CT-TU-08 Teste de Unidade para o Componente Gallery.vue:

* CT-TU-08-C1: verificar se o componente foi renderizado;
* CT-TU-08-C2: verificar se os botões estão renderizando;
* CT-TU-08-C3: verificar se as fotos estão sendo inseridas na entrada corretamente.
