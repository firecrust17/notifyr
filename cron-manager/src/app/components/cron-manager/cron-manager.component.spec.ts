import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CronManagerComponent } from './cron-manager.component';

describe('CronManagerComponent', () => {
  let component: CronManagerComponent;
  let fixture: ComponentFixture<CronManagerComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CronManagerComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CronManagerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
