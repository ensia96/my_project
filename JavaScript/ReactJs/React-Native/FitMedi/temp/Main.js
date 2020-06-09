import React, {Component} from 'react';
import {
  StyleSheet,
  View,
  Text,
  TouchableOpacity,
  ScrollView,
  Dimensions,
} from 'react-native';

import Nav from './Nav';

export default class Main extends Component {
  render() {
    return (
      <>
        <View style={styles.container}>
          <View style={styles.top}>
            <Text style={styles.title}>맞춤형 추천 루틴</Text>
          </View>
          <View style={styles.center}>
            <ScrollView>
              {[
                '처방 결과에 따른 추천 운동',
                '처방 결과에 따른 추천운동 1',
                '처방 결과에 따른 추천운동 2',
                '처방 결과에 따른 추천운동 11',
                '처방 결과에 따른 추천운동 11',
                '처방 결과에 따른 추천운동 11',
              ].map((title) => {
                return (
                  <>
                    <TouchableOpacity style={styles.content}>
                      <TouchableOpacity style={styles.sample}>
                        <Text style={styles.sample}>B</Text>
                      </TouchableOpacity>
                      <Text style={styles.ctitle}>{title}</Text>
                    </TouchableOpacity>
                  </>
                );
              })}
            </ScrollView>
          </View>
          <Nav />
        </View>
      </>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  top: {
    height: Dimensions.get('window').height / 12,
    justifyContent: 'flex-end',
    margin: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: 'black',
  },
  center: {
    width: Dimensions.get('window').width,
    flex: 1,
  },
  content: {
    width: '95%',
    height: 180,
    borderRadius: 10,
    backgroundColor: '#51cdd3',
    alignSelf: 'center',
    alignItems: 'flex-end',
    justifyContent: 'space-between',
    margin: 5,
  },
  ctitle: {
    margin: 10,
    fontSize: 20,
    color: 'white',
    fontWeight: 'bold',
    textAlignVertical: 'bottom',
  },
  sample: {
    margin: 3,
    color: 'white',
    fontSize: 34,
    fontWeight: '900',
  },
});
