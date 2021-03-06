import React, { Component } from "react"

class Select extends Component {

    constructor(){
      super();
      this.state = { options: [] };
    }

    componentWillMount(){
        var endpoint = "http://localhost:5000/v1/".concat(this.props.target).concat("/");

        fetch(endpoint)
          .then((response) => {
              return response.json()
          })
          .then((options) => {
              this.setState({options: options.results})
          });
    }

    render(){
        var name = this.props.name
        return (
            <div className="field">
              <label className="label">{this.props.label}:</label>
              <div className="control">
                <div className="select">
                  <select name={name} onChange={this.props.setOption} required>
                    <option value="">Selecione uma opção</option>
                    {this.state.options.map((item, index) => <option value={item.id}
                                                                     key={index}>{item[name]}</option>)}
                  </select>
                </div>
              </div>
            </div>
        )
    }
}

Select.propTypes = {
    label: React.PropTypes.string.isRequired,
    name: React.PropTypes.string.isRequired,
    target: React.PropTypes.string.isRequired
}

export default Select
