import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FileinfoComponent } from './fileinfo.component';

describe('FileinfoComponent', () => {
  let component: FileinfoComponent;
  let fixture: ComponentFixture<FileinfoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FileinfoComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(FileinfoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
