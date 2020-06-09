import React, {Component} from 'react';
import {
  StyleSheet,
  View,
  Text,
  TouchableOpacity,
  ScrollView,
  Dimensions,
} from 'react-native';

import Active from './Active';

export default class Main extends Component {
  render() {
    return (
      <>
        <View style={styles.container}>
          <View style={styles.top}>
            <View style={styles.titlewrapper}>
              <Text style={styles.title}>맞춤형 추천 루틴</Text>
              <Text style={styles.title}>
                한줄 18pt bold 기준 최대 16글자까지
              </Text>
            </View>
          </View>
          <View style={styles.center}>
            <ScrollView>
              {[
                {
                  title: '운동명사오육칠팔구십십일이삼',
                  dificulty: '초급',
                  sets: '10',
                  part: '어깨',
                },
                {
                  title: '운동명사오육칠팔구십십일이삼',
                  dificulty: '초급',
                  sets: '10',
                  part: '어깨',
                },
                {
                  title: '운동명사오육칠팔구십십일이삼',
                  dificulty: '초급',
                  sets: '10',
                  part: '어깨',
                },
                {
                  title: '운동명사오육칠팔구십십일이삼',
                  dificulty: '초급',
                  sets: '10',
                  part: '어깨',
                },
                {
                  title: '운동명사오육칠팔구십십일이삼',
                  dificulty: '초급',
                  sets: '10',
                  part: '어깨',
                },
              ].map((content) => {
                return (
                  <>
                    <TouchableOpacity style={styles.content}>
                      <View style={styles.imagewrapper}>
                        <Text style={{fontSize: 16, color: 'white'}}>
                          이미지
                        </Text>
                      </View>
                      <View style={styles.namewrapper}>
                        <Text style={styles.ctitle}>{content.title}</Text>
                        <View style={styles.itemwrapper}>
                          <Text style={styles.citems}>
                            {`난이도 : ${content.dificulty}\n부   위 : ${content.part}`}
                          </Text>
                          <Text style={styles.citems}>
                            세트수 : {content.sets}회
                          </Text>
                        </View>
                      </View>
                    </TouchableOpacity>
                  </>
                );
              })}
            </ScrollView>
          </View>
          <Active />
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
    flex: 1,
    width: Dimensions.get('window').width,
    justifyContent: 'flex-end',
    alignItems: 'flex-end',
    backgroundColor: '#33c1c8',
  },
  titlewrapper: {
    alignItems: 'flex-end',
    margin: 8,
  },
  title: {
    fontSize: 18,
    fontWeight: 'bold',
    color: 'white',
    margin: 3,
  },
  center: {
    width: Dimensions.get('window').width,
    flex: 1,
  },
  content: {
    width: '92%',
    height: 90,
    borderRadius: 10,
    alignSelf: 'center',
    // backgroundColor: '#51cdd3',
    flexDirection: 'row',
    margin: 5,
  },
  imagewrapper: {
    width: 76,
    alignItems: 'center',
    justifyContent: 'center',
    margin: 7,
    backgroundColor: '#2e2e2e',
    borderRadius: 10,
  },
  namewrapper: {
    margin: 10,
  },
  itemwrapper: {
    flex: 1,
    flexDirection: 'row',
    justifyContent: 'space-between',
    flexWrap: 'wrap',
    marginTop: 5,
  },
  ctitle: {
    fontSize: 18,
    color: 'black',
    fontWeight: 'bold',
    textAlignVertical: 'bottom',
  },
  citems: {
    color: '#444444',
    fontSize: 16,
  },
  sample: {
    margin: 3,
    color: 'white',
    fontSize: 34,
    fontWeight: '900',
  },
});
