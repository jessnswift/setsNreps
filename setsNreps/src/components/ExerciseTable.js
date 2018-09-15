import React, { Component } from "react";
import "react-bootstrap-table-next/dist/react-bootstrap-table2.min.css";
import BootstrapTable from "react-bootstrap-table-next";
import cellEditFactory, { Type } from "react-bootstrap-table2-editor";

export default class ExerciseTable extends Component {
  columns = [
    {
      dataField: "weight",
      text: "lbs"
    },
    {
      dataField: "reps",
      text: "reps"
    },
    {
      dataField: "complete",
      text: "completed",
      formatter: (cellContent, row) => (
        <div className="checkbox disabled">
          <label>
            <input type="checkbox" checked={ row.complete }/>
          </label>
        </div>
      )
    },
  ];

  onCellEdit = (oldValue, newValue, row, column) => {
    debugger;
    console.log('editing')
  }

  render() {
    return (
      <div>
        <div className="react-bootstrap-table">
          <h3>{this.props.exerciseDetails.exercise_name}</h3>
          <BootstrapTable
            keyField="id"
            data={this.props.exerciseDetails.sets}
            columns={this.columns}
            cellEdit={cellEditFactory({
              mode: "click",
              blurToSave: true,
              afterSaveCell: this.onCellEdit
              })}
          />
        </div>
      </div>
    );
  }
}