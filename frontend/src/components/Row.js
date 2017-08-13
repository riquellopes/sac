import React, { Component } from "react"

class Row extends Component {

    render(){
        var date = (new Date(this.props.created_date.split("+")[0])).toLocaleDateString("pt-BR", {
            hour: '2-digit',
            minute:'2-digit',
            second:'2-digit'
        });

        return (
            <tr>
                <td>{this.props.id}</td>
                <td>{this.props.type.type}</td>
                <td>{this.props.reason.reason}</td>
                <td>{this.props.country.country}</td>
                <td>{this.props.text}</td>
                <td>{date}</td>
            </tr>
        )
    }
}

export default Row
