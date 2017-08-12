import React, { Component } from 'react';
import { Link, IndexLink } from 'react-router';

class App extends Component {
  render() {
    return (
        <div>
            <nav className="nav has-shadow">
                <div className="nav-left">
                    <IndexLink to="/" className="nav-item is-tab" activeClassName="is-active">Atendimentos</IndexLink>
                    <Link to="/create" className="nav-item is-tab" activeClassName="is-active">Novo atendimento</Link>
                </div>
            </nav>

            <section className="section">
                <div className="container">
                    {this.props.children}
                </div>
            </section>
        </div>
    );
  }
}

export default App;
