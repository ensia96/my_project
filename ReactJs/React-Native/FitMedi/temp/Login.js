import React, {Component} from 'react';
import {
  SafeAreaView,
  StyleSheet,
  ScrollView,
  Alert,
  View,
  Text,
  StatusBar,
  Button,
  TouchableOpacity,
} from 'react-native';

export default class Login extends Component {
  render() {
    return (
      <>
        <StatusBar barStyle="light-content" />
        <View style={styles.container}>
          <View style={styles.part}>
            <Text style={styles.sample}>FM</Text>
            <Text style={styles.topt}>지금 회원가입하고</Text>
            <Text style={styles.topct}>
              맞춤형 운동관리
              <Text style={styles.topt}>를 받아보세요!</Text>
            </Text>
          </View>
          <View style={styles.part}>
            {[
              {name: '카카오톡 로그인'},
              {name: '구글 로그인'},
              {name: '페이스북 로그인'},
              {name: '애플 로그인'},
            ].map((thing, id) => {
              return (
                <TouchableOpacity
                  style={styles.cont}
                  onPress={() => {
                    Alert.alert(thing.name, '작업 중입니다.');
                  }}>
                  <Text key={id} style={styles.contt}>
                    {thing.name}
                  </Text>
                </TouchableOpacity>
              );
            })}
          </View>
          <View style={styles.btm}>
            <Text style={styles.btmt}>
              로그인하시면 개인정보처리방침 및 이용약관
            </Text>
            <Text style={styles.btmt}>
              그리고 저희의 더 나은 서비스 제공을 위한 연구정책에
            </Text>
            <Text style={styles.btmt}>동의하는 것으로 간주합니다.</Text>
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
  topt: {
    fontSize: 22,
    fontWeight: 'bold',
    color: 'white',
  },
  topct: {
    fontSize: 22,
    fontWeight: 'bold',
    color: '#35b3bc',
  },
  cont: {
    width: '85%',
    height: '26%',
    borderRadius: 30,
    borderColor: 'white',
    borderWidth: 1,
    margin: 4,
    justifyContent: 'center',
    alignItems: 'center',
  },
  contt: {
    color: 'white',
    fontSize: 23,
    fontWeight: 'bold',
  },
  part: {
    flex: 3,
    justifyContent: 'center',
    alignItems: 'center',
  },
  btm: {
    flex: 2,
    justifyContent: 'center',
    alignItems: 'center',
  },
  btmt: {
    justifyContent: 'center',
    color: 'white',
  },
  sample: {
    fontSize: 160,
    fontWeight: '900',
  },
});
