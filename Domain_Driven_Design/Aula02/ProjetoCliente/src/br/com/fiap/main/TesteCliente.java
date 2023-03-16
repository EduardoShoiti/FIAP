package br.com.fiap.main;

import br.com.fiap.modelo.Cliente;

public class TesteCliente {

	public static void main(String[] args) {
		
		Cliente objCliente = new Cliente();
		objCliente.setNome("Eduardo Shoiti");
		objCliente.setIdade(18);
		objCliente.setPeso(54.5);
		
		System.out.println("Nome: " + objCliente.getNome() + "\nIdade: " + objCliente.getIdade() + "\nPeso: " + objCliente.getPeso());

	}

}
