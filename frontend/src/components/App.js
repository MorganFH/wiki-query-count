import React, { Component } from "react";
import { render } from "react-dom";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      topic: "",
      section: "",
      data: {},
    };
  }

  execute_query(topic, section) {
    let url = `query?topic=${topic}`;
    if (section) {
      url += `&section=${section}`;
    }
    fetch(url)
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        this.setState(() => {
          return { data: data };
        });
      });
  }

  render() {
    return (
      <div>
        <h1>Wikipedia Topic occurences counter</h1>
        <form
          onSubmit={(e) => {
            e.preventDefault();
            this.execute_query(this.state.topic, this.state.section);
            this.setState(() => {
              return { topic: "", section: "" };
            });
          }}
        >
          <div>
            <input
              placeholder="Topic"
              value={this.state.topic}
              onChange={(e) =>
                this.setState(() => {
                  return { topic: e.target.value };
                })
              }
            />
          </div>
          <div>
            <input
              placeholder="Section"
              value={this.state.section}
              onChange={(e) =>
                this.setState(() => {
                  return { section: e.target.value };
                })
              }
            />
          </div>
          <button type="submit">Count wiki occurences</button>
        </form>
        {this.state.data.hits && (
          <div>
            <h2>
              Occurences of topic {this.state.data.topic}:{" "}
              {this.state.data.hits}
            </h2>
          </div>
        )}
      </div>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
