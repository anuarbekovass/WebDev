import { Component, OnInit } from '@angular/core';
import { Company } from '../company';
import { CompaniesService } from '../companies.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-company-list',
  templateUrl: './company-list.component.html',
  styleUrls: ['./company-list.component.css']
})
export class CompanyListComponent implements OnInit {

  constructor(private route: ActivatedRoute, private companiesService: CompaniesService) { }

  companies: Company[];

  ngOnInit(): void {
    this.getCompanies();
  }

  getCompanies(): void {
    this.companiesService.getCompanies().subscribe( companies => this.companies = companies);
  }
}
