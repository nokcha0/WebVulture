import React , { Component } from 'react'
import '../App.css';

class Tyler extends Component {
    constructor() {
        super()
        this.state = {
            message: 'Welcome to Paras',
            donut: 'HARROW'
        }
    }

    changeMessage() {
        this.setState({
            message: 'Welcome to Nowhere',
        })
    }

    render() {

        return (
            
        <div>
        <button onClick={() => {this.changeMessage()}}>Tyler Button</button>
        <h1>Tyler {this.state.message} {this.state.donut}</h1>
        </div>
    )}
}

export default Tyler