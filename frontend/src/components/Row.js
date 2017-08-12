import React, { Component } from "react"

class Row extends Component {

    render(){
        return (
            <tr>
                <td>{this.props.id}</td>
                <td>{this.props.type.type}</td>
                <td>{this.props.reason.reason}</td>
                <td>{this.props.country.country}</td>
                <td>{this.props.text}</td>
                <td>{this.props.created_date}</td>
            </tr>
        )
    }
}

export default Row
