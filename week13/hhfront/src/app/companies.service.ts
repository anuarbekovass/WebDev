import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { Company } from './company';
import { LoginResponse } from './login';

@Injectable({
  providedIn: 'root'
})
export class CompaniesService {

  constructor(private http: HttpClient) {
  }

  getCompanies(): Observable<Company[]> {
    return this.http.get<Company[]>('http://localhost:8000/api/companies/');
  }

  login(username, password): Observable<LoginResponse> {
    return this.http.post<LoginResponse>('http://localhost:8000/api/login/', {
      username,
      password
    });
  }
}
