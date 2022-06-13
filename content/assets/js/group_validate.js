
Vue.createApp({
  delimiters: ['[[', ']]'],
  data() {
    return {
      group: '',

      isGroupTouched: false
    }
  },
  methods: {
    blur() {
      this.isGroupTouched = true
    },
    validate() {
      if(this.group.includes('-')) {
        const group = this.group

        const groups = ['БД', 'Д', 'ИБА', 'ИБТ', 'ИКС', 'ИС', 'КМ', 'БУ', 'КС', 'МТ', 'ПИ', 'ПОКС', 'РТ', 'СА', 'УП']
        const conditionName = groups.some(groupName => groupName === group.split('-')[0].toUpperCase())

        const groupNumber = group.split('-')[1]

        const conditionNumber = groupNumber[0] < 4 &&
                                groupNumber[1] <= 9 &&
                                (groupNumber[2] ? !(groupNumber[2] >= 0) : true) &&
                                groupNumber.length <= 3


        if(this.isGroupTouched && (!conditionName || !conditionNumber)) return 'Такой группы не существует'
        return undefined
      } else {
        if(this.isGroupTouched) return 'Такой группы не существует'
        return undefined
      }
    }
  }
}).mount('#form')