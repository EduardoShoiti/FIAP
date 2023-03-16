package br.com.fiap.main;

import br.com.fiap.beans.Carro;
import br.com.fiap.beans.Motor;

public class TesteCarro {

	public static void main(String[] args) {
		
		Carro objetoCarro = new Carro();
		Motor objetoMotor = new Motor();
		
		objetoCarro.setMarca("FIAT");
		objetoCarro.setModelo("Uno");
		objetoCarro.setAno(2015);
		objetoCarro.setValor(27.555);
		objetoCarro.setMotor(objetoMotor);
		
		objetoMotor.setMarcaMotor("General Motors");
		objetoMotor.setPotencia(2.0);
		objetoMotor.setTipoCambio("Automatico");
		
		System.out.println("Marca do Carro: "+ objetoCarro.getMarca() +
				"\nModelo: "+ objetoCarro.getModelo() +
				"\nAno: " + objetoCarro.getAno() +
				"\nValor: "+ objetoCarro.getValor() +
				"\nMarca Motor: " + objetoCarro.getMotor().getMarcaMotor() +
				"\nPotencia Motor: "+ objetoCarro.getMotor().getPotencia() +
				"\nTipo Cambio: "+ objetoCarro.getMotor().getTipoCambio());

	}

}
