import { Component } from '@angular/core';
import { MatMenuModule } from '@angular/material/menu'; // For mat-menu and matMenuTriggerFor
import { MatButtonModule } from '@angular/material/button'; // For mat-button
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule } from '@angular/material/icon';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [
    MatMenuModule,
    MatButtonModule,
    MatToolbarModule,
    MatIconModule
  ],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.scss'
})
export class NavbarComponent {

}
