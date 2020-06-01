import React, {Component} from 'react';
import {
  SafeAreaView,
  StyleSheet,
  ScrollView,
  View,
  Text,
  StatusBar,
} from 'react-native';

export default class Loading extends Component {
  render() {
    return (
      <>
        <StatusBar barStyle="light-content" />
        <View style={styles.container}>
          <View style={styles.part}>
            {[
              {name: '근골격계', style: styles.mainWhiteFont},
              {name: '운동관리', style: styles.mainWhiteFont},
              {name: '피트메디', style: styles.mainNameFont},
            ].map((item) => {
              return <Text style={item.style}>{item.name}</Text>;
            })}
          </View>
          <View style={styles.part}>
            <Text style={styles.sample}>FM</Text>
          </View>
        </View>
      </>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#4e5355',
  },
  part: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  mainWhiteFont: {
    color: 'white',
    fontSize: 70,
  },
  mainNameFont: {
    color: '#35b3bc',
    fontSize: 70,
  },
  sample: {
    fontSize: 180,
    fontWeight: '900',
  },
});
