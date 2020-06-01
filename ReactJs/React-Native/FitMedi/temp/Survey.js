import React, {Component} from 'react';
import {
  SafeAreaView,
  StyleSheet,
  ScrollView,
  View,
  Text,
  StatusBar,
  TouchableOpacity,
  Alert,
  CheckBox,
} from 'react-native';

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
            <TouchableOpacity>
              <Text>다음으로</Text>
            </TouchableOpacity>
            <Text style={styles.btmt}>
              로그인하시면 개인정보처리방침 및 이용약관
            </Text>
          </View>
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
    flex: 2,
    justifyContent: 'center',
    alignItems: 'center',
  },
  btmt: {
    justifyContent: 'center',
  },
});
