import React, { Component } from "react"

import Form from "../components/Form"

class Create extends Component {

    render(){
        return (
            <div className="container is-fluid">
                <p className="title is-3">Sac</p>
                <p className="subtitle is-6">Novo atendimento</p>

                <Form />
            </div>
        )
    }
}

export default Create
