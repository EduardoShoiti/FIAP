package br.com.fiap.main;

import br.com.fiap.modelo.Cliente;
import br.com.fiap.modelo.Endereco;

public class TesteCliente {

	public static void main(String[] args) {
		
		Cliente objetoCliente = new Cliente();
		Endereco objetoEndereco = new Endereco();
		
		objetoCliente.setNome("Eduardo");
		objetoCliente.setIdade(18);
		objetoCliente.setPeso(51.4);
		objetoCliente.setEndereco(objetoEndereco);
		
		objetoEndereco.setLogradouro("Rua Apito do Vapor");
		objetoEndereco.setNumero(55);
		objetoEndereco.setBairro("Mooca");
		objetoEndereco.setMunicipio("São Paulo");
		
		System.out.println("Nome: " + objetoCliente.getNome() +
				"\nIdade: " + objetoCliente.getIdade() +
				"\nPeso: " + objetoCliente.getPeso() +
				"\nLogradouro: " + objetoCliente.getEndereco().getLogradouro() +
				"\nNúmero: " + objetoCliente.getEndereco().getNumero() +
				"\nBairro: " + objetoCliente.getEndereco().getBairro() +
				"\nMunicípio: " + objetoCliente.getEndereco().getMunicipio());

	}

}
