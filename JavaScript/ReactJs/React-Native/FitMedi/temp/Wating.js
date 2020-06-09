import React, {Component} from 'react';
import {StyleSheet, View, Text, StatusBar} from 'react-native';

export default class Wating extends Component {
  render() {
    return (
      <>
        <StatusBar barStyle="light-content" />
        <View style={styles.container}>
          <View style={styles.top}>
            <Text style={styles.text}>설문지 작성을</Text>
            <Text style={styles.text}>완료하셨습니다.</Text>
            <Text style={styles.text}> </Text>
            <Text style={styles.text}>고객님의 데이터를 바탕으로</Text>
            <Text style={styles.colored_text}>
              "맞춤형 운동 루틴"
              <Text style={styles.text}>을</Text>
            </Text>
            <Text style={styles.text}>준비하는 중 입니다.</Text>
            <Text style={styles.text}> </Text>
            <Text style={styles.text}>잠시만 기다려 주세요 :)</Text>
          </View>
          <View style={styles.btm}>
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
  text: {
    fontSize: 24,
    // fontWeight: 'bold',
    color: 'white',
  },
  colored_text: {
    fontSize: 24,
    // fontWeight: 'bold',
    color: '#35b3bc',
  },
  top: {
    flex: 3,
    justifyContent: 'center',
    alignItems: 'center',
  },
  btm: {
    flex: 2,
    justifyContent: 'center',
    alignItems: 'center',
  },
  sample: {
    fontSize: 160,
    fontWeight: '900',
  },
});
