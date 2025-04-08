import { Component, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Usuario } from './usuario'
import { UsuarioService } from './usuario.service'
import { JsonPipe } from '@angular/common';
import { TableModule } from 'primeng/table';
import { ButtonModule } from 'primeng/button';
import { IconField } from 'primeng/iconfield';
import { InputIcon } from 'primeng/inputicon';
import { FormsModule } from '@angular/forms';
import { InputTextModule } from 'primeng/inputtext';
import { Image, ImageModule } from 'primeng/image';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, 
    TableModule, 
    ButtonModule, 
    IconField, 
    InputIcon, 
    FormsModule, 
    InputTextModule, 
    ImageModule, 
    JsonPipe],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit {
  usuarios: Usuario[] = [];
  texto = ''
  usuarioSelecionado?: Usuario;
  
  constructor(private servico: UsuarioService) {
    
  }

  ngOnInit(): void {
    this.onGetUsuarios();
  }

  onGetUsuarios(): void {
    this.servico.getUsuarios().subscribe({
      next: (dados) => {
        this.usuarios = dados
      },
      error: (erro) => {
        console.log(erro)
      },
      complete: () => {
        console.log('Chamada finalizada.')
      }
    })
  }
}
