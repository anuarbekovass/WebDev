import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Vacancy } from './vacancy';

@Injectable({
  providedIn: 'root'
})
export class VacanciesService {

  constructor( private http: HttpClient ) { }

  vacancies: Vacancy[];
  private vacancyUrl = 'http://127.0.0.1:8000/api/vacancies/'

  getVacancies(): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>(this.vacancyUrl);
  }

  getVacanciesByCompany(id: number): Observable<Vacancy[]> {
    // const url = `${this.vacancyUrl}/?company=${id}`;
    const url = `http://127.0.0.1:8000/api/companies/${id}/vacancies/`;
    return this.http.get<Vacancy[]>(url);
  }
}
