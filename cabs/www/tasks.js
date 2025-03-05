import { createApp, ref } from 'vue';
import { TabButtons } from '@frappe/ui';

const App = {
    components: { TabButtons },
    setup() {
        const currentTab = ref('mytasks');

        return { currentTab };
    },
    template: `
        <div class="flex">
            <TabButtons
                :buttons="[
                    { label: 'Tasks assigned to me', value: 'mytasks' },
                    { label: 'Tasks created by me', value: 'created' }
                ]"
                v-model="currentTab"
            />
            <div v-if="currentTab === 'mytasks'">
                <p>Showing tasks assigned to you...</p>
            </div>
            <div v-if="currentTab === 'created'">
                <p>Showing tasks you created...</p>
            </div>
        </div>
    `
};

// Mount the Vue app
createApp(App).mount('#app');
