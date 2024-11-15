import { Component, OnChanges, OnInit, SimpleChanges } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { MatCommonModule } from '@angular/material/core';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import {MatSliderModule} from '@angular/material/slider';
interface Coordinate {
  x: number;
  y: number;
  metadata: {
    id: number;
    text: string;
  };
}

function getRandomInt(max: number) {
  return Math.floor(Math.random() * max);
}


function getRandomId(length: number) {
  let result = '';
  const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  const charactersLength = characters.length;
  let counter = 0;
  while (counter < length) {
    result += characters.charAt(Math.floor(Math.random() * charactersLength));
    counter += 1;
  }
  return result;
}

@Component({
  selector: 'app-mainpage',
  standalone: true,
  imports: [FormsModule, CommonModule, MatFormFieldModule, MatInputModule, MatSliderModule, MatCommonModule],
  templateUrl: './mainpage.component.html',
  styleUrl: './mainpage.component.scss'
})
export class MainpageComponent implements OnInit {
  id: string | null = "69";
  coords: Coordinate[] = [];
  inputValue : string = ""
  gridSize : number = 5
  grid: Coordinate[][][] = [[[]]]

  popupVisible = false;
  popupData: Coordinate[] = [];
  popupPosition = { x: 0, y: 0 };
  
  inputId: string = '';
  inputCoords: Coordinate[] = [{ x: 0, y: 0, metadata: {id: 0, text: "nothing"} }]; // Default one coordinate pair

  constructor(private route: ActivatedRoute, private router: Router) {}



  organizeCoordinates(): void {
    this.grid = Array.from({ length: this.gridSize }, () =>
      Array.from({ length: this.gridSize }, () => [])
    );
    // Multiply each coordinate by 100 and place it into a 10x10 grid
    this.coords.forEach(coord => {
      const gridX = Math.floor((coord.x * 100) / 100 * this.gridSize);
      const gridY = Math.floor((coord.y * 100) / 100 * this.gridSize);
      if (gridX >= 0 && gridX < this.gridSize && gridY >= 0 && gridY < this.gridSize) {
        this.grid[gridY][gridX].push(coord);
      }
    });
  }

  getCellSize(gs: number) {
    return `${10 * 50 / gs}px`
  }

  getGridRepeat() : string {
    return "repeat(" + `${this.gridSize}` + ", 50px);"
  }
  getBackgroundColor(count: number): string {
    const intensityR = 255 - Math.min(count * 15, 200); // Scale intensity by count, capped at 255
    const intensityB = 255 - Math.min((count * count), 250); // Scale intensity by count, capped at 255
    const intensityG = 255 - Math.min(count * 20, 250); // Scale intensity by count, capped at 255

    return `rgba(${intensityR}, ${intensityG}, ${intensityB}, 0.6)`; // Shades of blue
  }

  showPopup(coords: Coordinate[], event: MouseEvent) {
    if (coords.length > 0) {
      this.popupData = coords;
      this.popupPosition = { x: event.pageX + 10, y: event.pageY + 10 };
      this.popupVisible = true;
    }
  }

  hidePopup() {
    this.popupVisible = false;
  }

  randomCoords(n : number = 100) {
    for (let i = 0; i < n; ++i) {
      this.coords.push({x: Math.random(), y: Math.random(), metadata: {id: getRandomInt(1000), text: getRandomId(100)}})
    }
  }

  set _gridSize(value: number) {
    this.gridSize = value;
    this.organizeCoordinates()
  }

  ngOnInit(): void {


      this.route.queryParams.subscribe(params => {
          this.id = params['id'] ? params['id'] : "69";
          this.coords = params['coords'] ? JSON.parse(params['coords']) : [];
          this.inputId = this.id || '';
          this.inputCoords = this.coords || [{ x: 0, y: 0,  metadata: {id: 0, text: "nothing"} }];
      });
      this.randomCoords()
      this.organizeCoordinates()
  }

  addCoord() {
      this.inputCoords.push({ x: 0, y: 0 , metadata: {id: 0, text: "nothing"}});
  }

  removeCoord(index: number) {
      this.inputCoords.splice(index, 1);
  }

  onSubmit() {
      const coordsString = JSON.stringify(this.inputCoords);
      this.router.navigate([], {
          queryParams: { id: this.inputId, coords: coordsString },
          queryParamsHandling: 'merge' // Merge with other query params if needed
      });
  }
}
