import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class CronService {

	service_url = 'http://localhost:8001'

  constructor(private http: HttpClient,) { }

	private get_all_crons_url = `${this.service_url}/get_all_crons`;
  get_all_crons(payload) {
  	return this.http.post<any>(this.get_all_crons_url, payload);
  }

	private activate_cron_url = `${this.service_url}/activate_cron`;
  activate_cron(payload) {
  	return this.http.post<any>(this.activate_cron_url, payload);
  }

	private update_cron_url = `${this.service_url}/update_cron`;
  update_cron(payload) {
  	return this.http.post<any>(this.update_cron_url, payload);
  }

	private deactivate_cron_url = `${this.service_url}/deactivate_cron`;
  deactivate_cron(payload) {
  	return this.http.post<any>(this.deactivate_cron_url, payload);
  }


}
