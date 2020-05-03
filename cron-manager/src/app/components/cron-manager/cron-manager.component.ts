import { Component, OnInit } from '@angular/core';
import { CronService } from '../../services/cron.service';

@Component({
  selector: 'app-cron-manager',
  templateUrl: './cron-manager.component.html',
  styleUrls: ['./cron-manager.component.css']
})
export class CronManagerComponent implements OnInit {

	scripts_list:any = [];
	selected_index = -1;
	types = [
		{'name': 'Minutes', 'value': 'minute'},
		{'name': 'Hours', 'value': 'hour'},
		{'name': 'Day of month', 'value': 'dom'},
		{'name': 'Month', 'value': 'month'},
		{'name': 'Day of Week', 'value': 'dow'}
	];
	rules = [];

  constructor(
  	private cron: CronService,
  ) {
  	this.cron.get_all_crons({}).subscribe(res => {
  		if(res.success){
  			this.scripts_list = res.data;
  			console.log(res.data);
  		}
  	});
  }

  ngOnInit() {

  }

  test(i){
  	console.log(i, this.selected_index);
  }

  activate_cron(rules){
  	const index = this.selected_index;
		const payload = {
			'script': this.scripts_list[index]['script'],
			'rules': rules
		};
  	this.cron.activate_cron(payload).subscribe(res => {
  		if(res.success){
  			this.scripts_list[index] = res.data;
  			alert(res.message);
  		}
  	});
  }

  deactivate_cron(index){
  	this.selected_index = index;
		const payload = {
			'script': this.scripts_list[index]['script']
		};
  	this.cron.deactivate_cron(payload).subscribe(res => {
  		if(res.success){
  			this.scripts_list[index]['rules'] = null;
  			alert(res.message);
  		}
  	});
  }

  validate_rules(index){

  }

  

}
