import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';

@Component({
  selector: 'app-fileinfo',
  standalone: true,
  imports: [],
  templateUrl: './fileinfo.component.html',
  styleUrl: './fileinfo.component.scss'
})
export class FileinfoComponent implements OnInit{
  doc_id: string | null = null
  doc : any = {}
  topic : any = []
  sims : any = []

  constructor(private route: ActivatedRoute) {
  }

  async ngOnInit(): Promise<void> {
    this.route.params.subscribe(async (params: Params) =>  {
      this.doc_id = params['id']?.replaceAll("____", "/").replaceAll('----', '.')
      console.log(this.doc_id)
      let data = {
        path: this.doc_id?.replaceAll("____", "/").replaceAll('----', '.')
      }
      const resp = await fetch("/faiss/doctext", {
        method: "POST", // Use POST or another appropriate HTTP method
        headers: {
          "Content-Type": "application/json" // Ensure the server expects JSON
        },
        body: JSON.stringify(data) // Convert the data object to a JSON string
      });
      let r = await resp.json()
      console.log(r)
      this.doc = r["text"]
      this.topic = r["topics"]
      this.sims = r["sims"]
      console.log(this.doc, this.topic, this.sims)

    });
    
  }
}
