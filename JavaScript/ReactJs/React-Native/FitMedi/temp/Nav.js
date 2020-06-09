import React, {Component} from 'react';
import {
  StyleSheet,
  View,
  Text,
  TouchableOpacity,
  Dimensions,
} from 'react-native';

export default class Nav extends Component {
  state = {};
  render() {
    return (
      <>
        <View style={styles.container}>
          <TouchableOpacity style={styles.not_selected}>
            <Text style={styles.sample}>F</Text>
            <Text style={styles.not_selected}>haha</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.selected}>
            <Text style={styles.csample}>M</Text>
            <Text style={styles.selected}>haha</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.not_selected}>
            <Text style={styles.sample}>D</Text>
            <Text style={styles.not_selected}>haha</Text>
          </TouchableOpacity>
        </View>
      </>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    height: Dimensions.get('window').height / 11,
    flexDirection: 'row',
  },
  not_selected: {
    flex: 1,
    alignContent: 'center',
    margin: 3,
    fontSize: 12,
    textAlign: 'center',
    color: '#cecece',
  },
  selected: {
    flex: 1,
    alignContent: 'center',
    margin: 3,
    fontSize: 12,
    textAlign: 'center',
    color: '#51cdd3',
  },
  sample: {fontSize: 30, textAlign: 'center', color: '#cecece'},
  csample: {fontSize: 30, textAlign: 'center', color: '#51cdd3'},
});
