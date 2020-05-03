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
	rules:any = [];

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

  rules_empty() {
  	return {
  		"minute": {"type": "on", "value": ""},
  		"hour": {"type": "on", "value": ""},
  		"dom": {"type": "on", "value": ""},
  		"month": {"type": "on", "value": ""},
  		"dow": {"type": "on", "value": ""},
  	}
  }

  show_rules(i){
  	this.selected_index = i;
  	if(!this.scripts_list[this.selected_index]['rules']) {
  		this.rules = this.rules_empty();
  	} else {
  		this.rules = this.scripts_list[this.selected_index]['rules'];
  		this.encode_null_rules()
  	}
  }

  activate_cron(rules){
  	const index = this.selected_index;
		const payload = {
			'script': this.scripts_list[index]['script'],
			'rules': rules
		};
  	this.cron.activate_cron(payload).subscribe(res => {
  		if(res.success){
  			// this.scripts_list[index] = res.data;
  			this.scripts_list[index]['rules'] = rules;
  			this.selected_index = -1;
  			alert(res.message);
  		}
  	});
  }

  deactivate_cron(){
  	// this.selected_index = index;
		const payload = {
			'script': this.scripts_list[this.selected_index]['script']
		};
  	this.cron.deactivate_cron(payload).subscribe(res => {
  		if(res.success){
  			this.scripts_list[this.selected_index]['rules'] = null;
  			this.rules = this.rules_empty();
  			this.selected_index = -1;
  			alert(res.message);
  		}
  	});
  }

  update() {
  	if(this.validate_rules()){
  		this.update_cron(this.rules);
  	}
  }

  update_cron(rules){
		const index = this.selected_index;
		const payload = {
			'script': this.scripts_list[index]['script'],
			'rules': rules
		};
		this.cron.update_cron(payload).subscribe(res => {
			if(res.success){
				// this.scripts_list[index] = res.data;
				this.scripts_list[index]['rules'] = rules;
				this.selected_index = -1;
				alert(res.message);
			}
		});
  }

  activate() {
  	if(this.validate_rules()){
  		this.activate_cron(this.rules);
  	}
  }

  validate_rules(){
  	var valid = true;
  	this.decode_null_rules();
  	for(var i=0; i<this.types.length; i++){
  		if(this.rules[this.types[i]['value']]['type'] != null && this.rules[this.types[i]['value']]['value'] == ""){
  			valid = false;
  		}
  	}

  	if(!valid) {
  		alert("Fields cannot be left blank");
  	}
  	return valid;

  }


  encode_null_rules(){
  	for(var i=0; i<this.types.length; i++){
  		if(this.rules[this.types[i]['value']]['type'] == null){
  			this.rules[this.types[i]['value']]['type'] = "null";
  		}
  	}
  }
  
  decode_null_rules(){
  	for(var i=0; i<this.types.length; i++){
  		if(this.rules[this.types[i]['value']]['type'] == "null"){
  			this.rules[this.types[i]['value']]['type'] = null;
  		}
  	}
  }
  

}
