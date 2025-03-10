class TeaRecommender:
    """
    茶饮推荐系统，根据用户的个人信息和健康需求推荐合适的茶饮
    """
    
    def __init__(self):
        # 初始化茶饮数据库
        self.tea_database = {
            '绿茶': {
                'id': 1,
                'description': '绿茶富含抗氧化剂，有助于提高免疫力和促进新陈代谢。',
                'ingredients': ['茶叶', '嫩芽'],
                'benefits': ['抗氧化', '提神醒脑', '减肥瘦身'],
                'suitable_for': ['年轻人', '中年人', '减肥人群'],
                'taste_profile': ['清香', '微苦', '回甘']
            },
            '红茶': {
                'id': 2,
                'description': '红茶温和醇厚，有助于暖胃和促进消化。',
                'ingredients': ['发酵茶叶', '红茶茶芽'],
                'benefits': ['暖胃', '提神', '促进消化'],
                'suitable_for': ['中老年人', '胃寒人群'],
                'taste_profile': ['醇厚', '甜香', '微涩']
            },
            '菊花茶': {
                'id': 3,
                'description': '菊花茶具有清热解毒、明目的功效。',
                'ingredients': ['菊花', '蜂蜜(可选)'],
                'benefits': ['清热解毒', '明目', '降火'],
                'suitable_for': ['用眼过度人群', '肝火旺盛人群'],
                'taste_profile': ['甘甜', '清香', '微苦']
            },
            '普洱茶': {
                'id': 4,
                'description': '普洱茶有助于消化脂肪，降低血脂。',
                'ingredients': ['发酵普洱茶叶', '陈年茶饼'],
                'benefits': ['降脂', '助消化', '减肥'],
                'suitable_for': ['中老年人', '高脂血症人群'],
                'taste_profile': ['醇厚', '陈香', '回甘']
            },
            '乌龙茶': {
                'id': 5,
                'description': '乌龙茶有助于分解脂肪，促进新陈代谢。',
                'ingredients': ['半发酵茶叶', '乌龙茶芽'],
                'benefits': ['减肥', '降脂', '美容'],
                'suitable_for': ['肥胖人群', '中年人'],
                'taste_profile': ['清香', '果香', '回甘']
            },
            '白茶': {
                'id': 6,
                'description': '白茶性寒凉，具有清热解毒、降火的功效。',
                'ingredients': ['白毫银针', '白牡丹'],
                'benefits': ['抗氧化', '降火', '美容养颜'],
                'suitable_for': ['年轻人', '上火人群'],
                'taste_profile': ['清淡', '甜香', '清爽']
            },
            '枸杞茶': {
                'id': 7,
                'description': '枸杞茶滋补肝肾，明目养神。',
                'ingredients': ['枸杞子', '红枣(可选)', '冰糖(可选)'],
                'benefits': ['滋补肝肾', '明目', '养血'],
                'suitable_for': ['中老年人', '肝肾不足人群', '用眼过度人群'],
                'taste_profile': ['甘甜', '果香', '温和']
            },
            '薄荷茶': {
                'id': 8,
                'description': '薄荷茶清凉提神，有助于缓解头痛和消化不良。',
                'ingredients': ['薄荷叶', '蜂蜜(可选)'],
                'benefits': ['提神醒脑', '清热解毒', '缓解头痛'],
                'suitable_for': ['年轻人', '头痛人群', '消化不良人群'],
                'taste_profile': ['清凉', '薄荷香', '微甜']
            },
            '金银花茶': {
                'id': 9,
                'description': '金银花茶具有清热解毒、抗菌消炎的功效。',
                'ingredients': ['金银花', '菊花(可选)', '蜂蜜(可选)'],
                'benefits': ['清热解毒', '抗菌消炎', '降火'],
                'suitable_for': ['感冒初期人群', '咽喉肿痛人群'],
                'taste_profile': ['微苦', '清香', '回甘']
            },
            '玫瑰花茶': {
                'id': 10,
                'description': '玫瑰花茶有助于活血化瘀，调理气血，美容养颜。',
                'ingredients': ['玫瑰花', '冰糖(可选)'],
                'benefits': ['活血化瘀', '调理气血', '美容养颜'],
                'suitable_for': ['女性', '气血不畅人群'],
                'taste_profile': ['花香', '甜香', '清爽']
            }
        }
        
        # 初始化症状映射字典
        self.symptom_mapping = {
            '疲劳': ['绿茶', '红茶', '薄荷茶'],
            '免疫力低下': ['绿茶', '金银花茶'],
            '注意力不集中': ['绿茶', '薄荷茶'],
            '肥胖': ['绿茶', '普洱茶', '乌龙茶'],
            '体重超标': ['绿茶', '普洱茶', '乌龙茶'],
            '胃寒': ['红茶'],
            '消化不良': ['红茶', '普洱茶', '薄荷茶'],
            '胃胀': ['红茶', '普洱茶'],
            '上火': ['菊花茶', '白茶', '金银花茶'],
            '咽喉疼痛': ['菊花茶', '金银花茶'],
            '口腔溃疡': ['菊花茶', '金银花茶'],
            '眼睛疲劳': ['菊花茶', '枸杞茶'],
            '视力模糊': ['菊花茶', '枸杞茶'],
            '口干舌燥': ['白茶', '菊花茶'],
            '高血脂': ['普洱茶', '乌龙茶'],
            '皮肤暗沉': ['乌龙茶', '玫瑰花茶'],
            '皮肤干燥': ['乌龙茶', '玫瑰花茶'],
            '腰膝酸软': ['枸杞茶'],
            '头晕目眩': ['枸杞茶'],
            '面色苍白': ['枸杞茶', '玫瑰花茶'],
            '头痛': ['薄荷茶'],
            '偏头痛': ['薄荷茶'],
            '感冒初期': ['金银花茶'],
            '气血不畅': ['玫瑰花茶']
        }
    
    def get_recommendations(self, form_data):
        """
        根据用户提交的表单数据生成茶饮推荐
        
        Args:
            form_data (dict): 包含用户信息和健康需求的表单数据
            
        Returns:
            list: 推荐的茶饮列表，每个元素为包含茶名和描述的字典
        """
        # 提取表单数据
        age = form_data.get('age')
        gender = form_data.get('gender')
        symptoms = form_data.get('symptoms', [])
        taste_preference = form_data.get('taste_preference')
        goals = form_data.get('goals')
        
        # 根据用户数据筛选合适的茶饮
        recommendations = []
        
        # 根据症状推荐
        if symptoms:
            for tea_name, tea_info in self.tea_database.items():
                # 检查茶饮的功效是否匹配用户的症状
                for benefit in tea_info['benefits']:
                    if self._is_benefit_match_symptoms(benefit, symptoms):
                        recommendations.append({
                            'name': tea_name,
                            'description': tea_info['description'],
                            'reason': f'适合缓解{", ".join(symptoms)}'
                        })
                        break
        
        # 根据口味偏好推荐
        if taste_preference and not recommendations:
            for tea_name, tea_info in self.tea_database.items():
                if taste_preference in tea_info['taste_profile']:
                    recommendations.append({
                        'name': tea_name,
                        'description': tea_info['description'],
                        'reason': f'符合您{taste_preference}的口味偏好'
                    })
        
        # 根据养生目标推荐
        if goals and not recommendations:
            for tea_name, tea_info in self.tea_database.items():
                for benefit in tea_info['benefits']:
                    if benefit in goals:
                        recommendations.append({
                            'name': tea_name,
                            'description': tea_info['description'],
                            'reason': f'有助于实现{goals}的养生目标'
                        })
                        break
        
        # 如果没有匹配的推荐，提供一些通用推荐
        if not recommendations:
            # 根据年龄段提供通用推荐
            if age and age.isdigit():
                age_num = int(age)
                if age_num < 30:
                    recommendations.append({
                        'name': '绿茶',
                        'description': self.tea_database['绿茶']['description'],
                        'reason': '适合年轻人饮用，有助于提高免疫力'
                    })
                elif age_num < 50:
                    recommendations.append({
                        'name': '乌龙茶',
                        'description': self.tea_database['乌龙茶']['description'],
                        'reason': '适合中年人饮用，有助于控制体重'
                    })
                else:
                    recommendations.append({
                        'name': '枸杞茶',
                        'description': self.tea_database['枸杞茶']['description'],
                        'reason': '适合老年人饮用，有滋补养生的功效'
                    })
            else:
                # 默认推荐
                recommendations.append({
                    'name': '绿茶',
                    'description': self.tea_database['绿茶']['description'],
                    'reason': '绿茶是最常见的健康茶饮，适合大多数人'
                })
        
        return recommendations[:3]  # 最多返回3个推荐
    
    def _is_benefit_match_symptoms(self, benefit, symptoms):
        """
        判断茶饮的功效是否匹配用户的症状
        
        Args:
            benefit (str): 茶饮功效
            symptoms (list): 用户的症状列表
            
        Returns:
            bool: 是否匹配
        """
        benefit_symptom_map = {
            '抗氧化': ['疲劳', '免疫力低下'],
            '提神醒脑': ['疲劳', '注意力不集中'],
            '减肥瘦身': ['肥胖', '体重超标'],
            '暖胃': ['胃寒', '消化不良'],
            '促进消化': ['消化不良', '胃胀'],
            '清热解毒': ['上火', '咽喉疼痛', '口腔溃疡'],
            '明目': ['眼睛疲劳', '视力模糊'],
            '降火': ['上火', '口干舌燥'],
            '降脂': ['高血脂', '肥胖'],
            '助消化': ['消化不良', '胃胀'],
            '美容': ['皮肤暗沉', '皮肤干燥'],
            '滋补肝肾': ['腰膝酸软', '头晕目眩'],
            '养血': ['面色苍白', '头晕'],
            '缓解头痛': ['头痛', '偏头痛'],
            '抗菌消炎': ['咽喉疼痛', '感冒初期'],
            '活血化瘀': ['气血不畅', '面色苍白'],
            '调理气血': ['气血不畅', '面色苍白']
        }
        
        if benefit in benefit_symptom_map:
            for symptom in symptoms:
                if symptom in benefit_symptom_map[benefit]:
                    return True
        
        return False