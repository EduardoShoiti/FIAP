package br.com.fiap.main;

import br.com.fiap.modelo.Cliente;

public class TesteCliente {

	public static void main(String[] args) {
		
		Cliente objCliente = new Cliente();
		
//		Entrada
		objCliente.setNome("Eduardo");
		objCliente.setIdade(18);
		
//		Saida
		System.out.println(objCliente.getNome());
		System.out.println(objCliente.getIdade());
	}

}
