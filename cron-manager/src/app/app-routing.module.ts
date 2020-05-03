import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { CronManagerComponent } from './components/cron-manager/cron-manager.component';

const routes: Routes = [
	{
		path: '**',
		component: CronManagerComponent
	}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
