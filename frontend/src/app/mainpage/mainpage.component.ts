import { Component, OnChanges, OnInit, SimpleChanges } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { MatCommonModule } from '@angular/material/core';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import {MatSliderModule} from '@angular/material/slider';
import { NavbarComponent } from '../navbar/navbar.component';
import {MatExpansionModule} from '@angular/material/expansion';

interface Coordinate {
  x: number;
  y: number;
  metadata: {
    id: number;
    text: string;
    file: string;
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
  imports: [FormsModule, 
    CommonModule, 
    MatFormFieldModule, 
    MatInputModule, 
    MatSliderModule, 
    MatCommonModule,
    NavbarComponent,
    MatExpansionModule,
  ],
  templateUrl: './mainpage.component.html',
  styleUrl: './mainpage.component.scss',
})
export class MainpageComponent implements OnInit {
  id: string | null = "69";
  coords: Coordinate[] = [];
  inputValue : string = ""
  gridSize : number = 5
  grid: Coordinate[][][] = [[[]]]

  cellResolution: number = 70
  maxCellLength: number = 10

  popupVisible = false;
  popupData: Coordinate[] = [];
  popupPosition = { x: 0, y: 0 };
  
  inputId: string = '';
  inputCoords: Coordinate[] = [{ x: 0, y: 0, metadata: {id: 0, text: "nothing", file: "file"} }]; // Default one coordinate pair

  evns = new Map<string, any>()

  constructor(private route: ActivatedRoute, private router: Router) {}



  organizeCoordinates(): void {
    this.grid = Array.from({ length: this.gridSize }, () =>
      Array.from({ length: this.gridSize }, () => [])
    );
    this.maxCellLength = 1
    // Multiply each coordinate by 100 and place it into a 10x10 grid
    console.log("weretwsfgdhytresfdgdhryetrswgf")
    this.coords.forEach(coord => {
      const gridX = Math.min(Math.floor((coord.x * 100) / 100 * this.gridSize), this.gridSize);
      const gridY = Math.min(Math.floor((coord.y * 100) / 100 * this.gridSize), this.gridSize);
      console.log(coord.x, coord.y, gridX, gridY, this.gridSize)
      if (gridX >= 0 && gridX < this.gridSize && gridY >= 0 && gridY < this.gridSize) {
        this.grid[gridY][gridX].push(coord);
        this.maxCellLength = Math.max(this.maxCellLength, this.grid[gridY][gridX].length)
      }
    });
    console.log("weretwsfgdhytresfdgdhryetrswgf")

    
  }

  async requestDocs() {
    let data = {
      "query" : this.inputValue
    }
    const resp = await fetch("/faiss/query", {
      method: "POST", // Use POST or another appropriate HTTP method
      headers: {
        "Content-Type": "application/json" // Ensure the server expects JSON
      },
      body: JSON.stringify(data) // Convert the data object to a JSON string
    });
    
    let documents = await resp.json()
    let docs = documents["message"];
    console.log(documents)
    
    this.coords = []
    let maxx = 0;
    for (let i = 0; i < Math.min(75, docs.length); ++i) {
        maxx = Math.max(parseInt(docs[i][1]), maxx)
    }
    
    for (let i = 0; i < Math.min(75, docs.length); ++i) {
      console.log(docs[i], parseInt(docs[i][1]) / (maxx + 1))
      this.coords.push({
        x: parseInt(docs[i][1]) / (maxx + 1), 
        y: Math.random(), 
        metadata: {
          id: 1,
          text: docs[i][1],
          file: docs[i][0] 
        }})
    }

    // this.randomCoords()
    console.log("---------\n")
    console.log(this.coords, this.coords.length)
    console.log("---------\n")
    this.organizeCoordinates()
  }

  getCellSize(gs: number, off: number = 0) {
    return `${10 * this.cellResolution / gs + off}px`
  }

  getTransform(gs: number, nmax: number = 10, grids : number = -1) {
    if (gs / nmax < 0.138) {
      return `scale(0)`;
    }
    let sc = Math.min(1.0, 1 + Math.log(gs / nmax) / Math.log(10));
    let tz = 1;
    if (grids > 0){
      tz = parseInt(this.getCellSize(grids).substring(0, this.getCellSize(grids).length-2)) / 18;
    }
    return `scale(${sc * tz})`
  }

  getGridRepeat() : string {
    return "repeat(" + `${this.gridSize}` + `, ${this.cellResolution}px);`
  }
  getBackgroundColor(count: number): string {
    count = count * 10 / this.maxCellLength
    const intensityR = 255 - Math.min(count * 15, 200); // Scale intensity by count, capped at 255
    const intensityB = 255 - Math.min((count * count), 250); // Scale intensity by count, capped at 255
    const intensityG = 255 - Math.min(count * 20, 250); // Scale intensity by count, capped at 255
    return `rgba(${intensityR}, ${intensityG}, ${intensityB}, 0.6)`; // Shades of blue
  }

  showPopup(coords: Coordinate[], event: MouseEvent | null = null) {
    if (coords.length > 0) {
      this.popupData = coords;
      if (event) {
        this.evns.set("popup", true)
        this.popupVisible = true
        this.popupPosition = { x: event.pageX - 10, y: event.pageY - 10 };
      }
      this.popupVisible = true;
    }
  }

  hidePopup() {
    this.popupVisible = false;
  }

  randomCoords(n : number = 50) {
    for (let i = 0; i < n; ++i) {
      this.coords.push({x: Math.random(), y: Math.random(), metadata: {id: getRandomInt(1000), text: getRandomId(100), file: "file"}})
    }
  }

  set _gridSize(value: number) {
    this.gridSize = value;
    this.organizeCoordinates()
  }

  ngOnInit(): void {
      
      this.organizeCoordinates()
  }

  addCoord() {
      this.inputCoords.push({ x: 0, y: 0 , metadata: {id: 0, text: "nothing", file: "file"}});
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
