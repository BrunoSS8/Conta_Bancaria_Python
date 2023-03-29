# Conta_Bancaria_Python
 O código é um programa em Python que simula uma conta bancária 
 
 
O código é um programa em Python que simula uma conta bancária com opções para criar uma conta, depositar, sacar, verificar o saldo e verificar o rendimento da conta poupança.<br><br>
O programa utiliza três classes: Conta, ‘ContaCorrente’ e ‘ContaPoupanca’. A classe Conta é a classe base, que contém o ID da conta e o saldo da conta, e as classes ‘ContaCorrente’ e ‘ContaPoupanca’ são subclasses que herdam de Conta e adicionam funcionalidades específicas para cada tipo de conta. <br><br>
A função <strong>’criar_conta()’</strong> cria uma nova conta com base nas informações fornecidas pelo usuário. Ele solicita o ID da conta, o saldo inicial e o tipo de conta. Se o tipo de conta é corrente, cria uma nova conta corrente, senão, cria uma nova conta poupança. Em seguida, adiciona a conta recém-criada à lista de contas existentes. <br><br>
A função <strong> ‘menu()’ </strong> exibe as opções disponíveis para o usuário e solicita uma entrada do usuário. <br><br>
O loop principal do programa começa em seguida, onde é exibido o menu e a opção selecionada pelo usuário é tratada. Se a opção for '1', a função <strong>’criar_conta()’ </strong> é chamada e a nova conta é adicionada à lista de contas existentes. Se a opção for '2', é solicitado o ID da conta e o valor a depositar e o saldo da conta é atualizado. Se a opção for '3', é solicitado o ID da conta e o valor a sacar, e o saldo da conta é atualizado de acordo. Se a opção for '4', é solicitado o ID da conta e o saldo da conta é exibido na tela. Se a opção for '5', é solicitado o ID da conta e o período (em segundos, minutos, horas, dias, semanas, meses ou anos) para o qual o rendimento da conta poupança deve ser exibido. Se a conta não for encontrada ou não for uma conta poupança, uma mensagem de erro será exibida. <br><br>
O programa continuará em loop até que o usuário escolha a opção de sair (opção '0').

