import { Routes } from '@angular/router';
import { MainpageComponent } from './mainpage/mainpage.component';
import { FileinfoComponent } from './fileinfo/fileinfo.component';

export const routes: Routes = [
    {path: '', component: MainpageComponent},
    {path: 'docs/:id', component: FileinfoComponent},
];
