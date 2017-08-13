import React, { Component } from "react"

import Select from "./Select"

class Form extends Component {

    constructor() {
        super();

        this.state = {
            type_called_id: 0,
            country_id: 0,
            reason_id: 0,
            text: "",
            display: "none"
        }

        this.handlerSubmit = this.handlerSubmit.bind(this);
    }
    handlerSubmit(event) {
        event.preventDefault();

        console.info(this.state);

        fetch("http://localhost:5000/v1/recordcalled/", {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.state)
            })
            .then((response) => {
                return response.json()
            })
            .then((json) => {
                this.beforeResponse(json);
            })
            .catch((error) => {
                console.error("Fail", error);
            });
    }

    beforeResponse(response){
        this.refs.form.reset();
        this.setState({
            type_called_id: 0,
            country_id: 0,
            reason_id: 0,
            text: "",
            display: "block"
        });
    }

    handlerTextArea(event){
        this.setState({text: event.target.value});
    }

    handlerType(event){
        this.setState({type_called_id: event.target.value});
    }

    handlerCountry(event){
        this.setState({country_id: event.target.value});
    }

    handlerReason(event){
        this.setState({reason_id: event.target.value});
    }

    handleClick(event){
        this.setState({"display": "none"});
    }

    render(){
        return (
            <div>
                <div className="notification is-success" style={{display:this.state.display}}>
                  <button className="delete" onClick={this.handleClick.bind(this)}></button>
                  Atendimento registrado com sucesso.
                </div>
                <form onSubmit={this.handlerSubmit} ref="form">

                    <Select label="Tipo"
                            name="type"
                            target="type-called"
                            setOption={this.handlerType.bind(this)}/>
                    <Select label="Cidade"
                            name="country"
                            target="countries"
                            setOption={this.handlerCountry.bind(this)}/>
                    <Select label="Motivo"
                            target="reasons"
                            name="reason"
                            setOption={this.handlerReason.bind(this)}/>

                    <div className="field">
                      <label className="label">Messagem: </label>
                      <div className="control">
                        <textarea className="textarea"
                                  placeholder="Informações sobre o contato."
                                  name="text"
                                  value={this.state.text}
                                  onChange={this.handlerTextArea.bind(this)} required></textarea>
                      </div>
                    </div>
                    <br />
                    <div className="field">
                        <div className="control">
                            <p className="control">
                                <input type="submit" value="salvar" className="button is-primary"/>
                            </p>
                        </div>
                    </div>
                </form>
            </div>
        )
    }
}

export default Form
