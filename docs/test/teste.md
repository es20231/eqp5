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

## Testes Manuais

### CT-TM-01 Teste Manual de Cadastro:

* CT-TM-01-C1: verificar se um novo cadastro está sendo feito;
* CT-TM-01-C2: verificar se a validação de _username_ está sendo feita;
* CT-TM-01-C3: verificar se a validação de _name_ está sendo feita;
* CT-TM-01-C4: verificar se a validação de _email_ está sendo feita;
* CT-TM-01-C5: verificar se a validação de senha está sendo feita;
* CT-TM-01-C6: verificar se a validação de confirmação de senha está seneo feita;
* CT-TM-01-C7: verificar se a validação de cadastro está sendo feita.

### CT-TM-02 Teste Manual de Login:

* CT-TM-02-C1: verificar se o login está sendo feito;
* CT-TM-02-C2: verificar se a validação de _email_ está sendo feita;
* CT-TM-02-C3: verificar se a validação de senha está sendo feita;
* CT-TM-02-C4: verificar se a validação de login está sendo feita.

### CT-TM-03 Teste Manual de Upload:

* CT-TM-03-C1: verificar se o _upload_ está sendo feito;
* CT-TM-03-C2: verificar se a imagem está sendo exibida após o _upload_;
* CT-TM-03-C3: verificar se a função _delete_ está funcionando normalmente;
* CT-TM-03-C4: verificar se é permitido fazer _upload_ de mais de uma imagem;
* CT-TM-03-C5: verificar se a paginação está funcionando;
* CT-TM-03-C6: verificar se é possível fazer multiplos _uploads_.

## Teste de Integração

### CT-TI-01 Teste de Integração de Cadastro:

* CT-TI-01-C1: verificar se um novo cadastro está sendo feito;
* CT-TI-01-C2: verificar se a validação de _username_ está sendo feita;
* CT-TI-01-C3: verificar se a validação de _name_ está sendo feita;
* CT-TI-01-C4: verificar se a validação de _email_ está sendo feita;
* CT-TI-01-C5: verificar se a validação de senha está sendo feita;
* CT-TI-01-C6: verificar se a validação de confirmação de senha está seneo feita;
* CT-TI-01-C7: verificar se a validação de cadastro está sendo feita.

### CT-TI-02 Teste de Integração de Login:

* CT-TI-02-C1: verificar se o login está sendo feito;
* CT-TI-02-C2: verificar se a validação de _email_ está sendo feita;
* CT-TI-02-C3: verificar se a validação de senha está sendo feita;
* CT-TI-02-C4: verificar se a validação de login está sendo feita.

### CT-TI-03 Teste Integração de Upload:

* CT-TI-03-C1: verificar se o _upload_ está sendo feito;
* CT-TI-03-C2: verificar se a imagem está sendo exibida após o _upload_;
* CT-TI-03-C3: verificar se a função _delete_ está funcionando normalmente;
* CT-TI-03-C4: verificar se é permitido fazer _upload_ de mais de uma imagem;
* CT-TI-03-C5: verificar se a paginação está funcionando;
* CT-TI-03-C6: verificar se é possível fazer multiplos _uploads_.

## Testes de Sistema

### CT-TS-01 Teste de Sistema de Cadastro:

* CT-TS-01-C1: verificar se o cadastro está funcionando conforme o fluxo principal;
* CT-TS-01-C2: verificar se o _link_ de login está funcionando conforme o fluxo alternativo;

## CT-TS-02: Teste de Sistema de Login:

* CT-TS-02-C1: verificar se o login está funcionando conforme o fluxo principal;
* CT-TS-02-C2: verificar se o _link_ de recuperação de senha está funcionando conforme o fluxo alternativo;
* CT-TS-02-C3: verificar se o _link_ de cadastro está funcionando conforme o fluxo alternativo.

## CT-TS-03: Teste de Sistema de Upload:

* CT-TS-03-C1: verificar se a função _delete_ está funcionando conforme o fluxo alternativo;
* CT-TS-03-C2: verificar se a paginação está funcionando conforme o fluxo alternativo.
