import React, {Component} from 'react';
import {StyleSheet, View, Text, TouchableOpacity, Alert} from 'react-native';

import Active from './Active';

export default class Survey extends Component {
  state = {
    checked: true,
  };
  render() {
    return (
      <>
        <View style={styles.container}>
          <View style={styles.qcon}>
            <Text style={styles.qnum}>Q1</Text>
            <Text style={styles.qtext}>운동 목적을 알려줄래요?</Text>
            <Text style={styles.qtext}>(중복선택 가능)</Text>
          </View>
          <View style={styles.ccon}>
            {[
              '근육량 증가',
              '다이어트',
              '근력증가(스트렝스)',
              '몸매관리',
              '홈트레이닝/맨몸',
              '질환/통증관리',
            ].map((item) => {
              return (
                <TouchableOpacity
                  style={styles.citem}
                  onPress={() => {
                    Alert.alert('haha');
                  }}>
                  <View style={styles.checkbox} />
                  <Text style={styles.ctext}>{item}</Text>
                </TouchableOpacity>
              );
            })}
          </View>
          <View style={styles.btm}>
            <View style={{flexDirection: 'row'}}>
              <View style={styles.now} />
              <View style={styles.all} />
              <View style={styles.all} />
              <View style={styles.all} />
            </View>
          </View>
          <Active />
        </View>
      </>
    );
  }
}

const styles = StyleSheet.create({
  checkbox: {
    width: 20,
    height: 20,
    color: 'black',
    alignSelf: 'center',
    borderColor: 'black',
    borderWidth: 1,
    borderRadius: 3,
    backgroundColor: 'black',
    marginRight: 10,
  },
  container: {
    flex: 1,
  },
  qcon: {
    flex: 3,
    justifyContent: 'flex-end',
    marginLeft: '7%',
  },
  qnum: {
    color: '#36b9c2',
    fontSize: 100,
    fontWeight: 'bold',
  },
  qtext: {
    fontSize: 27,
    fontWeight: 'bold',
  },
  ccon: {
    flex: 4,
    justifyContent: 'center',
    marginLeft: '7%',
  },
  citem: {
    flexDirection: 'row',
    margin: '3%',
  },
  ctext: {
    fontSize: 20,
  },
  btm: {
    flex: 1,
    justifyContent: 'flex-end',
    alignItems: 'center',
  },
  all: {
    backgroundColor: '#e8e8e8',
    width: 12,
    height: 12,
    borderRadius: 6,
    margin: 10,
  },
  now: {
    backgroundColor: '#26c1c9',
    width: 12,
    height: 12,
    borderRadius: 6,
    margin: 10,
  },
  next: {
    width: '85%',
    height: 40,
    margin: 3,
    borderRadius: 20,
    backgroundColor: '#c5c5c5',
    justifyContent: 'center',
    alignItems: 'center',
  },
  nextt: {
    color: 'white',
    fontSize: 18,
    fontWeight: 'bold',
  },
});
