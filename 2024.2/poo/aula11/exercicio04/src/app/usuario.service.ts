import { Injectable } from '@angular/core';
import { Observable, map } from 'rxjs';
import { Usuario } from './usuario';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class UsuarioService {

  constructor(private http: HttpClient) { }

  getUsuarios(): Observable<Usuario[]> {
    return this.http.get<Usuario[]>('https://reqres.in/api/users?per_page=12')
    .pipe(map((retorno: any) => retorno.data)); 
  }
}
