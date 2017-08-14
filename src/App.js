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

    this.socket = new WebSocket('ws://10.0.1.181:5678/');
  }

  componentWillMount() {
    this.readTextFile()
  }

  readTextFile() {
    let txtFile = require('./Server/ip.json');
    console.log(txtFile.ip)
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
    const Sound = require('./Sound.html');
    return (
      <View style={styles.container}>
        <Text>Virtual Reality</Text>
        <Text>{this.state.data}</Text>
        <WebView
          source={Sound}
          style={{flex: 1}}
        />
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
