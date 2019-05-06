import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-dataframe-display',
  templateUrl: './dataframe-display.component.html'
})
export class DataFrameDisplayComponent implements OnInit {

  @Input() dataFrame: any;
  rowLimit: number = 25;
  startIndex: number = 0;
  endIndex: number = 25;
  rowIndices: number[];

  generateRowIndices() {
    this.rowIndices = [];
    for (let count=this.startIndex; count<this.endIndex; count++) {
      this.rowIndices.push(count);
    }
  }

  ngOnInit() {
    this.generateRowIndices();
  }

  nextRows() {
    this.startIndex += this.rowLimit;
    this.endIndex += this.rowLimit;
    if (this.endIndex >= this.dataFrame['data'].length) {
      this.endIndex = this.dataFrame['data'].length;
    }
    this.generateRowIndices();
  }

  previousRows() {
    this.startIndex -= this.rowLimit;
    this.endIndex -= this.rowLimit;
    if (this.startIndex <= 0) {
      this.startIndex = 0;
    }
    this.generateRowIndices();
  }

}