import React, { Component } from 'react';
import {
  StyleSheet,
  Text,
  View,
  WebView
} from 'react-native';

class App extends Component {
  constructor() {
    super();
    this.state = {
      open: false,
      data: null,
    };
    this.socket = new WebSocket('ws://127.0.0.1:5678/');
  }

  componentDidMount() {
    this.socket.onopen = () => this.socket.send(JSON.stringify({type: 'greet', payload: 'Hello Mr. Server!'}));
    this.socket.onmessage = ({data}) => this.processData(data);
  }

  processData(data) {
    this.setState({
      ...this.state,
      data: data
    })
  }

  render() {


    return (
      <View style={styles.container}>
        <Text>Virtual Reality</Text>
        <Text>{this.state.data}</Text>
      </View>
    );
  }
}


const styles = StyleSheet.create({
  container: {
    paddingTop: 20,
    flex: 1,
  }
});

export default App;
