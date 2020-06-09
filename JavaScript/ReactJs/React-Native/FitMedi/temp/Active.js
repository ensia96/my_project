import React, {Component} from 'react';
import {
  StyleSheet,
  View,
  Text,
  TouchableOpacity,
  Dimensions,
} from 'react-native';

export default class Active extends Component {
  state = {};
  render() {
    return (
      <>
        <View style={styles.container}>
          <TouchableOpacity style={styles.not_selected}>
            <Text style={styles.not_selected_text}>다음으로</Text>
          </TouchableOpacity>
        </View>
      </>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    height: Dimensions.get('window').height / 11,
    alignItems: 'center',
  },
  not_selected: {
    width: '85%',
    height: 40,
    margin: 3,
    borderRadius: 20,
    backgroundColor: '#cecece',
    justifyContent: 'center',
    alignItems: 'center',
  },
  not_selected_text: {
    fontSize: 18,
    fontWeight: 'bold',
    color: 'white',
  },
  selected: {
    width: '85%',
    height: 40,
    margin: 3,
    borderRadius: 20,
    backgroundColor: '#51cdd3',
    justifyContent: 'center',
    alignItems: 'center',
  },
  selected_text: {
    fontSize: 18,
    fontWeight: 'bold',
    color: 'white',
  },
});
