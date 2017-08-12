import React, { Component } from "react"

// Components
import Grid from "../components/Grid"

class Home extends Component {

    constructor(){
      super();
      this.state = { recordscalled: [] };
    }

    componentWillMount(){
      fetch("http://localhost:5000/v1/recordcalled/")
        .then((response) => {
            return response.json()
        })
        .then((recordscalled) => {
            this.setState( {recordscalled: recordscalled.results})
        });
    }

    render(){
        return (
            <div className="container is-fluid">
                <p className="title is-3">Sac</p>
                <p className="subtitle is-6">Atendimentos</p>
                <Grid list={this.state.recordscalled}/>
            </div>
        )
    }
}

export default Home
